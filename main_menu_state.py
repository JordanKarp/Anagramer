from state import State
from user import User
from util import clear_terminal, input_ranged_int


class MainMenuState(State):
    def __init__(self):
        super().__init__()

    def print_header(self):
        print("Welcome To Anagramer!")
        print("~~~~~~~" * 6)

    def run(self):
        clear_terminal()
        self.print_header()

        choice = input_ranged_int("1. New Game\n2. Quit\n", 1, 2)
        if choice == 1:
            name = input("Who is playing?\n")
            self.persist["user"] = User(name)
            self.next_state = "GAME_MENU"
        elif choice == 2:
            self.next_state = "QUIT"
