
from explorerphatdashboard.frames.explorerphat import ExplorerPhat
from explorerphatdashboard.frames.main import Main
from scriptcore.guiscript import GuiScript


class Dashboard(GuiScript):

    def __init__(self, base_path, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param arguments:   The arguments
        """

        title = 'Explorer Phat Dashboard'
        description = 'A dashboard for Explorer PHAT (Explorer HAT)'

        super(Dashboard, self).__init__(base_path, title, description, arguments=arguments)

        self.config.load_from_ini(self.get_path('config.ini'))

    def _init(self):
        """
        Initiate the dashboard
        """

        main = Main(self._screen)
        explorer_phat = ExplorerPhat(self._screen)

        self._add_scene([main.get_view()], name="Dashboard")
        self._add_scene([explorer_phat.get_view()], name="ExplorerPhat Dashboard")
