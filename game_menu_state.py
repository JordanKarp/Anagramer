from state import State
from util import clear_terminal, input_ranged_int


class GameMenuState(State):
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

    def print_header(self):
        print(f"Game Menu for {self.user.name}")
        print(f"Words Known: {self.user.words_known}")
        print(f"Words Value: {self.user.words_known_value}")
        print("~~~~~~~" * 6)

    def run(self):
        clear_terminal()
        self.print_header()
        choice = input_ranged_int(
            "1. New Round\n2. Upgrade Menu\n3. View User Collected Vocabulary\n4. Quit\n",
            1,
            4,
        )
        if choice == 1:
            num = input_ranged_int("Game Size (3-15)\n", 3, 15)
            self.persist["round_size"] = int(num)
            self.next_state = "GAME"
        elif choice == 2:
            self.next_state = "UPGRADE_MENU"
        elif choice == 3:
            self.user.print_vocab()
            input()
        elif choice == 4:
            self.next_state = "QUIT"
