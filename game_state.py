from game_round import GameRound
from state import State
from util import clear_terminal

WORD_FILE = "wordList.txt"


def load_words(word_file):
    with open(word_file, "r") as f:
        dictionary = f.read()
    return [x.lower() for x in dictionary.split("\n")]


class GameState(State):
    def __init__(self):
        super().__init__()
        self.user = None
        self.round_size = None
        self.round = None
        self.all_words = load_words(WORD_FILE)

    def startup(self, persistent=None):
        """Upon state startup"""
        if persistent is None:
            persistent = {}
        self.next_state = self
        self.persist = persistent
        self.user = self.persist["user"]
        self.round_size = self.persist["round_size"]
        self.round = GameRound(self.round_size, self.all_words, self.user)

        self.round.preguess_user_words()

    def run(self):
        clear_terminal()
        if self.round.round_won():
            print("Great Job!")
            for word in self.round.all_anagrams:
                self.user.add_word(word)
            self.next_state = "GAME_MENU"
            self.persist["user"] = self.user
        else:
            self.round.print_round_letters()
            self.round.print_round_anagrams()
            keep_guessing = self.round.guess_word()
            if not keep_guessing:
                self.next_state = "QUIT"
