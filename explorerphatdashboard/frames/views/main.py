
from scriptcore.console.asciimatics.widgets.button import Button
from scriptcore.console.asciimatics.widgets.frame import Frame
from scriptcore.console.asciimatics.widgets.layout import Layout


class Main(Frame):

    def __init__(self,
                 screen,
                 on_load=None,
                 on_explorerphat_click=None,
                 on_exit=None):
        """
        Initiate the frame
        :param screen:
        """
        super(Main, self).__init__(screen,
                                   'Dashboard',
                                   on_load=on_load)

        self._on_explorerphat_click = on_explorerphat_click
        self._on_exit = on_exit

        self._add_header("Options")
        self._add_options()
        self._add_exit()

        self.fix()

    def _add_options(self):

        layout = Layout([1])
        self.add_layout(layout)
        layout.add_widget(Button("ExplorerPhat", self._on_explorerphat_click))

    def _add_exit(self):
        """
        Add the exit button
        :return:
        """

        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)

        layout2 = Layout([1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Exit", self._on_exit))
