from scriptcore.console.asciimatics.widgets.button import Button
from scriptcore.console.asciimatics.widgets.frame import Frame
from scriptcore.console.asciimatics.widgets.layout import Layout
from scriptcore.console.asciimatics.widgets.text import Text


class ExplorerPhat(Frame):

    def __init__(self,
                 screen,
                 on_load=None,
                 on_output_toggle=None,
                 on_motor_min_click=None,
                 on_motor_plus_click=None,
                 on_exit=None):
        """
        Initiate the frame
        :param screen:
        """
        super(ExplorerPhat, self).__init__(screen,
                                           'ExplorerPhat Dashboard',
                                           on_load=on_load)

        self._on_output_toggle = on_output_toggle
        self._on_motor_min_click = on_motor_min_click
        self._on_motor_plus_click = on_motor_plus_click
        self._on_exit = on_exit

        self._add_header('Inputs')
        self._add_inputs()
        self._add_divider()
        self._add_header('Outputs')
        self._add_outputs()
        self._add_divider()
        self._add_header('Analogs')
        self._add_analogs()
        self._add_divider()
        self._add_header('Motors')
        self._add_motors()
        self._add_exit()

        self.fix()

    def _add_inputs(self):
        """
        Add the inputs
        :return:
        """

        self._inputs = dict()
        self._inputs[1] = Text('Input 1')
        self._inputs[2] = Text('Input 2')
        self._inputs[3] = Text('Input 3')
        self._inputs[4] = Text('Input 4')

        layout = Layout([1, 9])
        self.add_layout(layout)
        for text in self._inputs.values():
            layout.add_widget(text, 1)

    def _add_outputs(self):
        """
        Add the outputs
        :return:
        """

        self._outputs = dict()
        self._outputs[1] = Text('Output 1')
        self._outputs[2] = Text('Output 2')
        self._outputs[3] = Text('Output 3')
        self._outputs[4] = Text('Output 4')

        def on_output_toggle(output_id):
            if self._on_output_toggle is not None:
                self._on_output_toggle(output_id)

        self._output_buttons = dict()
        self._output_buttons[1] = Button('Toggle 1', lambda: on_output_toggle(1))
        self._output_buttons[2] = Button('Toggle 2', lambda: on_output_toggle(2))
        self._output_buttons[3] = Button('Toggle 3', lambda: on_output_toggle(3))
        self._output_buttons[4] = Button('Toggle 4', lambda: on_output_toggle(4))

        layout = Layout([1, 4, 5])
        self.add_layout(layout)
        for output_id in self._outputs:

            layout.add_widget(self._outputs[output_id], 1)
            layout.add_widget(self._output_buttons[output_id], 2)

    def _add_analogs(self):
        """
        Add the analogs
        :return:
        """

        self._analogs = dict()
        self._analogs[1] = Text('Analog 1')
        self._analogs[2] = Text('Analog 2')
        self._analogs[3] = Text('Analog 3')
        self._analogs[4] = Text('Analog 4')

        layout = Layout([1, 9])
        self.add_layout(layout)
        for text in self._analogs.values():
            layout.add_widget(text, 1)

    def _add_motors(self):
        """
        Add the motors
        :return:
        """

        self._motors = dict()
        self._motors[1] = Text('Motor 1')
        self._motors[2] = Text('Motor 2')

        def on_motor_min_click(motor_id):
            if self._on_motor_min_click is not None:
                self._on_motor_min_click(motor_id)

        self._motor_min_buttons = dict()
        self._motor_min_buttons[1] = Button('-10 1', lambda: on_motor_min_click(1))
        self._motor_min_buttons[2] = Button('-10 2', lambda: on_motor_min_click(2))

        def on_motor_plus_click(motor_id):
            if self._on_motor_plus_click is not None:
                self._on_motor_plus_click(motor_id)

        self._motor_plus_buttons = dict()
        self._motor_plus_buttons[1] = Button('+10 1', lambda: on_motor_plus_click(1))
        self._motor_plus_buttons[2] = Button('+10 2', lambda: on_motor_plus_click(2))

        layout = Layout([1, 3, 3, 3])
        self.add_layout(layout)
        for motor_id in self._motors:
            layout.add_widget(self._motors[motor_id], 1)
            layout.add_widget(self._motor_min_buttons[motor_id], 2)
            layout.add_widget(self._motor_plus_buttons[motor_id], 3)

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

    def get_input_ids(self):

        return self._inputs.keys()

    def set_input(self, input_id, value):

        self._inputs[input_id].value = '%s' % value

    def get_output_ids(self):

        return self._outputs.keys()

    def set_output(self, output_id, value):

        self._outputs[output_id].value = '%s' % value

    def get_analog_ids(self):

        return self._analogs.keys()

    def set_analog(self, analog_id, value):

        self._analogs[analog_id].value = '%.3f V' % value

    def get_motor_ids(self):

        return self._motors.keys()

    def set_motor(self, motor_id, value):

        self._motors[motor_id].value = '%i' % value
