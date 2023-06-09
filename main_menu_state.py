import pickle
from pathlib import Path

from state import State
from user import User
from util import clear_terminal, input_ranged_int

SAVES_PATH = Path(".") / "saves"


class MainMenuState(State):
    def __init__(self):
        super().__init__()
        self.persist["saves_path"] = SAVES_PATH

    def print_header(self):
        print("Welcome To Anagramer!")
        print("~~~~~~~" * 6)

    def prompt_name(self):
        return input("Who is playing?\n")

    def load_user(self, name):
        while True:
            try:
                filename = f"{name}.dat"
                with open(SAVES_PATH / filename, "rb") as f:
                    user_data = pickle.load(f)
            except FileNotFoundError:
                print("Game not found, starting a new game instead?")
                play = input("[y/n]\n")
                if play in ["y", "Y"]:
                    return User(name)
                else:
                    name = self.prompt_name()
            else:
                return user_data

    def run(self):
        clear_terminal()
        self.print_header()

        print('1. New Game\n2. Load Game\n3. High Scores\n4. Quit\n')
        choice = input_ranged_int('> ', 1, 4)
        if choice == 1:
            name = self.prompt_name()
            self.persist["user"] = User(name)
            self.next_state = "GAME_MENU"
        elif choice == 2:
            name = self.prompt_name()
            self.persist["user"] = self.load_user(name)
            self.next_state = "GAME_MENU"
        elif choice == 3:
            self.next_state = "HIGH_SCORE"
        elif choice == 4:
            self.next_state = "QUIT"
