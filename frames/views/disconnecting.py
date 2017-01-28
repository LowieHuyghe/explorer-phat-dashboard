
from scriptcore.console.asciimatics.widgets.popupdialog import PopUpDialog


class Disconnecting(PopUpDialog):

    def __init__(self, screen):
        """
        Initiate the connecting dialog
        :param screen:
        """

        super(Disconnecting, self).__init__(screen,
                                            "Disconnecting...",
                                            [])
