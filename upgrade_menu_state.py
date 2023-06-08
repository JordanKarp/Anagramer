from state import State


class UpgradeMenuState(State):
    def __init__(self):
        super().__init__()
        self.user = None

    def startup(self, persistent=None):
        """Upon state startup"""
        if persistent is None:
            persistent = {}
        self.next_state = self
        self.persist = persistent
        self.user = self.persist["user"]

    def run(self):
        print("Upgrade menu TBI")
        input()
        self.next_state = "GAME_MENU"
