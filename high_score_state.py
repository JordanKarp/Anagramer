from state import State


class HighScoreState(State):
    def __init__(self):
        super().__init__()

    def startup(self, persistent=None):
        """Upon state startup"""
        if persistent is None:
            persistent = {}
        self.next_state = self
        self.persist = persistent

    def run(self):
        print("High Score TBI")
        input()
        self.next_state = "MAIN_MENU"
