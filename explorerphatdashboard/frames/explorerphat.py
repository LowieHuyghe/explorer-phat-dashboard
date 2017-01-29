
import time
from threading import Thread
from explorerphatdashboard.api.explorerphat.analog import Analog as ApiAnalog
from explorerphatdashboard.api.explorerphat.connection import Connection
from explorerphatdashboard.api.explorerphat.input import Input as ApiInput
from explorerphatdashboard.api.explorerphat.motor import Motor as ApiMotor
from explorerphatdashboard.api.explorerphat.output import Output as ApiOutput
from explorerphatdashboard.frames.views.connecting import Connecting as ConnectingView
from explorerphatdashboard.frames.views.disconnecting import Disconnecting as DisconnectingView
from explorerphatdashboard.frames.views.explorerphat import ExplorerPhat as ExplorerPhatView
from scriptcore.console.asciimatics.framelogic import FrameLogic


class ExplorerPhat(FrameLogic):
    """
    The logic for the ExplorerPhatFrame
    """

    def __init__(self, screen):
        """
        Initiate the explorer phat frame
        :param screen:
        """

        super(ExplorerPhat, self).__init__(screen)

        self._view = ExplorerPhatView(self._screen,
                                      on_load=self._on_load,
                                      on_output_toggle=self._on_output_toggle,
                                      on_motor_min_click=self._on_motor_min_click,
                                      on_motor_plus_click=self._on_motor_plus_click,
                                      on_exit=self._on_exit)
        self._connection = Connection.get_connection()

    def get_view(self):
        """
        Get the view
        :return:
        """

        return self._view

    def _on_load(self):
        """
        On load
        :return:
        """

        self._open_connection()

    def _open_connection(self):
        """
        Open connection
        :return:
        """

        connecting_view = ConnectingView(self._screen, on_cancel=lambda x: self._on_exit())
        self._view.add_effect_to_scene(connecting_view)

        def open_connection():
            self._connection.open()
            self._update_all_items()
            connecting_view.close()
            self._on_connected()

        thread = Thread(target=open_connection)
        thread.start()

    def _on_connected(self):
        """
        On connected
        :return:
        """

        self._start_auto_update()

    def _start_auto_update(self):
        """
        Start the auto update
        :return:
        """

        def update():
            while self._connection.is_open():
                self._update_all_items()
                time.sleep(0.5)

        thread = Thread(target=update)
        thread.start()

    def _update_all_items(self):
        """
        Update all items
        :return:
        """

        for input_id in self._view.get_input_ids():
            self._view.set_input(input_id, (ApiInput(input_id)).on)
        for output_id in self._view.get_output_ids():
            self._view.set_output(output_id, (ApiOutput(output_id)).on)
        for analog_id in self._view.get_analog_ids():
            self._view.set_analog(analog_id, (ApiAnalog(analog_id)).value)
        for motor_id in self._view.get_motor_ids():
            self._view.set_motor(motor_id, (ApiMotor(motor_id)).speed)

    def _on_output_toggle(self, output_id):
        """
        On output toggle
        :param output_id:
        :return:
        """

        (ApiOutput(output_id)).toggle()
        # This is a fix so the dashboard keeps updating.
        self._view._outputs[output_id].focus()

    def _on_motor_min_click(self, motor_id):
        """
        On motor min click
        :param motor_id:
        :return:
        """

        motor = ApiMotor(motor_id)
        speed = motor.speed

        speed -= 10
        if speed < -100:
            speed = -100
        motor.speed = speed

        # This is a fix so the dashboard keeps updating.
        self._view._motors[motor_id].focus()

    def _on_motor_plus_click(self, motor_id):
        """
        On motor plus click
        :param motor_id:
        :return:
        """

        motor = ApiMotor(motor_id)
        speed = motor.speed

        speed += 10
        if speed > 100:
            speed = 100
        motor.speed = speed

        # This is a fix so the dashboard keeps updating.
        self._view._motors[motor_id].focus()

    def _on_exit(self):
        """
        On exit click
        :return:
        """

        disconnecting_view = DisconnectingView(self._screen)
        self._view.add_effect_to_scene(disconnecting_view)
        self._connection.close()
        disconnecting_view.close()

        self._change_scene("Dashboard")
