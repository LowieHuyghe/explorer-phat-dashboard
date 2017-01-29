
import subprocess
import random
import string
import time
import threading
from scriptcore.basescript import BaseScript


class Connection(object):

    connection = None
    connection_lock = threading.Lock()

    @staticmethod
    def get_connection():
        """
        Create a connection
        :return: Connection
        """
        if Connection.connection is None:
            with Connection.connection_lock:
                if Connection.connection is None:
                    current_script = BaseScript.current_script()
                    host = current_script.config.get('ssh.host')
                    user = current_script.config.get('ssh.user')
                    port = current_script.config.get('ssh.port', 22)
                    Connection.connection = Connection(host, user, port)
        return Connection.connection

    def __init__(self, host, user, port=None):
        """
        Construct the constructor
        :param host:
        :param user:
        :param port:
        """

        self._host = host
        self._user = user
        self._port = port
        self._ssh = None
        self._ssh_lock = threading.Lock()

    def is_open(self):
        return self._ssh is not None

    def open(self):
        if self._ssh is not None:
            return False

        with self._ssh_lock:
            if self._ssh is not None:
                return False

            ssh = subprocess.Popen(["ssh", "-tt", "-p %i" % self._port, "%s@%s" % (self._user, self._host)],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            random_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            ssh.stdin.write('sudo python -c \'exec("import explorerhat\\nprint \\"%s\\"\\nwhile True: exec(raw_input())")\' && exit || exit\n' % random_string)

            waited = 0
            while waited < 10:
                if random_string in ssh.stdout.readline():
                    break
                time.sleep(0.1)
                waited += 0.1

            if waited < 10:
                self._ssh = ssh
                return True
            else:
                ssh.terminate()
                ssh.wait()
                return False

    def close(self):
        if self._ssh is None:
            return False

        with self._ssh_lock:
            if self._ssh is None:
                return False

            if self._ssh.poll() is None:
                self._ssh.stdin.write('exit()\n')
                time.sleep(0.2)

            if self._ssh.poll() is None:
                self._ssh.terminate()
                self._ssh.wait()

            self._ssh = None

            return True

    def run(self, python_code):

        if self._ssh is None:
            return False
        elif self._ssh.poll() is not None:
            self.close()
            return False

        with self._ssh_lock:
            if self._ssh is None:
                return False
            elif self._ssh.poll() is not None:
                self.close()
                return False

            start_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            stop_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            self._ssh.stdin.write('print "%s"; %s; print "%s"\n' % (start_string, python_code, stop_string))

            output = None
            while True:
                line = self._ssh.stdout.readline()
                if start_string in line:
                    output = ''
                elif stop_string in line:
                    break
                elif output is not None:
                    if output == '':
                        output += line.strip()
                    else:
                        output += '\n' + line.strip()

            # Convert the output
            if output == "":
                output = None
            else:
                try:
                    output = int(output)
                except ValueError:
                    try:
                        output = float(output)
                    except ValueError:
                        pass

            return output
