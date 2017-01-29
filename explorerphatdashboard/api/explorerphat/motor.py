
from explorerphatdashboard.api.explorerphat.connection import Connection


class Motor(object):

    def __init__(self, id):

        self._id = id
        self._name = self._get_name_from_id(id)

    def _get_name_from_id(self, id):
        if id == 1:
            return 'one'
        if id == 2:
            return 'two'

    @property
    def speed(self):
        connection = Connection.get_connection()
        return int(connection.run('print explorerhat.motor.%s._speed' % self._name))

    @speed.setter
    def speed(self, value):
        connection = Connection.get_connection()
        connection.run('explorerhat.motor.%s.speed(%i)' % (self._name, value))

    def forwards(self, value):
        connection = Connection.get_connection()
        connection.run('explorerhat.motor.%s.forwards(%i)' % (self._name, value))

    def backwards(self, value):
        connection = Connection.get_connection()
        connection.run('explorerhat.motor.%s.backwards(%i)' % (self._name, value))

    def stop(self):
        connection = Connection.get_connection()
        connection.run('explorerhat.motor.%s.stop()' % self._name)

    def inverse(self):
        connection = Connection.get_connection()
        connection.run('explorerhat.motor.%s.inverse()' % self._name)
