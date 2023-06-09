import pickle

from state import State
from util import clear_terminal, input_ranged_int


class GameMenuState(State):
    def __init__(self):
        super().__init__()
        self.user = None
        self.saves_path = None

    def startup(self, persistent=None):
        """Upon state startup"""
        if persistent is None:
            persistent = {}
        self.next_state = self
        self.persist = persistent
        self.user = self.persist["user"]
        self.saves_path = self.persist["saves_path"]

    def print_header(self):
        print(f"Game Menu for {self.user.name}")
        print(f"Words Known: \t{self.user.words_known}")
        print(f"Words Value: \t{self.user.words_known_value}")
        print(f"Points: \t{self.user.points}")
        print("~~~~~~~" * 6)

    def print_upgrades(self):
        print(f"Freebies (f): \t{self.user.freebies}")
        print(f"Extra Time (t): {self.user.extra_times}")
        print(f"Extra Lives: \t{self.user.extra_lives}")
        print("~~~~~~~" * 6)

    def print_menu(self):
        print('1. New Round')
        print('2. Upgrade Menu')
        print('3. View collected words')
        print('4. Save and Quit')
        print('5. Score and Quit')

    def print_instructions(self):
        clear_terminal()
        print("Rearrange the letters and make make every possible word before time runs out.")
        print("Every word 'collected' will make future rounds easier!")
        print("~~~~~~~" * 6)
        print(f"Press 'f' to use a freebie, if available: ({self.user.freebies})")
        print(f"Press 't' to get 30 seconds extra time, if available: ({self.user.extra_times})")
        print("Press 'q' to give up.")
        print("~~~~~~~" * 6)

    def run(self):
        clear_terminal()
        self.print_header()
        self.print_upgrades()
        self.print_menu()

        choice = input_ranged_int('> ', 1, 5)
        if choice == 1:
            self.print_instructions()
            print('How many letters would you like to play (3-15)?')
            num = input_ranged_int("> ", 3, 15)
            self.persist["round_size"] = num
            self.next_state = "GAME"
        elif choice == 2:
            self.next_state = "UPGRADE_MENU"
        elif choice == 3:
            clear_terminal()
            self.user.print_vocab()
            input('-- ')
        elif choice == 4:
            filename = f"{self.user.name}.dat"
            with open(self.saves_path / filename, "wb") as f:
                pickle.dump(self.user, f)
            print(f"{self.user.name}'s game saved.")
            self.next_state = "QUIT"
        elif choice == 5:
            # TODO SAVE SCORE
            self.next_state = "HIGH_SCORE"
