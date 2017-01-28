
from api.explorerphat.connection import Connection
from frames.views.main import Main as MainView
from scriptcore.console.asciimatics.framelogic import FrameLogic


class Main(FrameLogic):
    """
    The logic for the MainFrame
    """

    def __init__(self, screen):
        """
        Initiate the explorer phat frame
        :param screen:
        """

        super(Main, self).__init__(screen)

        self._view = MainView(self._screen,
                              on_explorerphat_click=self._on_explorerphat_click,
                              on_exit=self._on_exit)
        self._connection = Connection.get_connection()

    def get_view(self):
        """
        Get the view
        :return:
        """

        return self._view

    def _on_explorerphat_click(self):
        """
        On explorer-phat click
        :return:
        """

        self._change_scene("ExplorerPhat Dashboard")

    def _on_exit(self):
        """
        On exit click
        :return:
        """

        exit()
