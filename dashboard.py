
from frames.explorerphat import ExplorerPhat
from frames.main import Main
from scriptcore.console.guiscript import GuiScript
import os.path


class Dashboard(GuiScript):

    def __init__(self, base_path):
        """
        Construct the script
        :param base_path:   The base path
        """

        super(Dashboard, self).__init__(base_path)

        self.config.load_from_ini(self.get_path('config.ini'))

    def _init(self):
        """
        Initiate the dashboard
        """

        main = Main(self._screen)
        explorer_phat = ExplorerPhat(self._screen)

        self._add_scene([main.get_view()], name="Dashboard")
        self._add_scene([explorer_phat.get_view()], name="ExplorerPhat Dashboard")


# Run the Dashboard
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(__file__))
    (Dashboard(base_path)).run()
