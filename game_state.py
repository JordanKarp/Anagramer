from game_round import GameRound
from game_timer import GameTimer
from state import State
from util import clear_terminal

WORD_FILE = "wordList.txt"
TIMEPERLETTER = 120.0
BASETIME = -300.0


def load_words(word_file):
    with open(word_file, "r") as f:
        dictionary = f.read()
    return [x.lower() for x in dictionary.split("\n")]


def timer_length(word_size):
    return TIMEPERLETTER * word_size + BASETIME


class GameState(State):
    def __init__(self):
        super().__init__()
        self.user = None
        self.round_size = None
        self.round = None
        self.timer = None
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
        self.timer = GameTimer(timer_length(self.round_size), self.round_lost)
        self.timer.start()

    def round_lost(self):
        # TODO submit high score
        # TODO delete save file
        print('Sorry, you lose.')
        input('-- ')
        self.next_state = 'HIGH_SCORE'

    def save_words_to_user(self):
        for word in self.round.all_anagrams:
            self.user.add_word(word)

    def run(self):
        clear_terminal()
        if self.round.is_round_won():
            self.timer.cancel()
            print("Great Job!")
            self.save_words_to_user()
            self.next_state = "GAME_MENU"
            self.persist["user"] = self.user
        elif self.timer.expired:
            self.round_lost()
        else:
            self.round.print_round_letters()
            print(f'Time remaining: {self.timer.remaining}')
            self.round.print_round_anagrams()
            keep_guessing = self.round.guess_word()
            if not keep_guessing:
                if self.user.can_use_extra_life():
                    self.user.extra_lives -= 1
                    print(f'Extra life used! {self.user.extra_lives} remaining.')
                    input('-- ')
                    self.next_state = "GAME_MENU"
                else:
                    self.next_state = "QUIT"
                    
    def cleanup(self):
        self.timer.cancel()
