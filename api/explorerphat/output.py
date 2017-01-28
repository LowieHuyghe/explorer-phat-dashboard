
from connection import Connection


class Output(object):

    def __init__(self, id):

        self._id = id
        self._name = self._get_name_from_id(id)

    def _get_name_from_id(self, id):
        if id == 1:
            return 'one'
        if id == 2:
            return 'two'
        if id == 3:
            return 'three'
        if id == 4:
            return 'four'

    @property
    def on(self):
        connection = Connection.get_connection()
        return bool(connection.run('print explorerhat.output.%s.read()' % self._name))

    @on.setter
    def on(self, value):
        connection = Connection.get_connection()
        if value:
            connection.run('print explorerhat.output.%s.on()' % self._name)
        else:
            connection.run('print explorerhat.output.%s.off()' % self._name)

    def toggle(self):
        connection = Connection.get_connection()
        connection.run('print ( explorerhat.output.%s.off() if explorerhat.output.%s.read() else explorerhat.output.%s.on() )' % (self._name, self._name, self._name))
