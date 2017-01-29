
from scriptcore.console.asciimatics.widgets.popupdialog import PopUpDialog


class Connecting(PopUpDialog):

    def __init__(self, screen, on_cancel=None):
        """
        Initiate the connecting dialog
        :param screen:
        :param on_cancel:
        """

        super(Connecting, self).__init__(screen,
                                         "Connecting...",
                                         ["Cancel"],
                                         on_click=on_cancel)
