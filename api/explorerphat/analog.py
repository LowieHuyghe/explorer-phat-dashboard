
from connection import Connection


class Analog(object):

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
    def value(self):
        connection = Connection.get_connection()
        return float(connection.run('print explorerhat.analog.%s.read()' % self._name))
