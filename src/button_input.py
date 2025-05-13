class ButtonInput:
    def __init__(self):
        self.button_states = {}

    def update_button_state(self, button_id, state):
        self.button_states[button_id] = state

    def is_button_pressed(self, button_id):
        return self.button_states.get(button_id, False)

    def reset_button_states(self):
        self.button_states.clear()