from random import choice, shuffle
from collections import Counter

BLANK_CHAR = "_"


class GameRound:
    def __init__(self, size, all_words, user):
        self.size = size
        self.all_words = all_words
        self.user = user
        self.letters = self.anagram_letters()
        self.all_anagrams = self.get_all_anagrams()
        self.num_anagrams = len(self.all_anagrams)

    def anagram_letters(self):
        wrd = choice(self.all_words)
        while len(wrd) != self.size:
            wrd = choice(self.all_words)
        letters = list(wrd.upper())
        shuffle(letters)
        return letters

    def get_all_anagrams(self):
        MIN_WORD_LENGTH = 2
        letters = "".join(self.letters)
        letters = letters.lower()
        count = Counter(letters)

        all_anagrams = set()
        for word in self.all_words:
            if not set(word) - set(letters):
                check_word = {k for k, v in Counter(word).items() if v <= count[k]}
                if check_word == set(word):
                    all_anagrams.add(word)

        anagram_list = [x for x in all_anagrams if len(x) >= MIN_WORD_LENGTH]
        sorted_list = sorted(anagram_list, key=lambda x: len(x), reverse=True)

        return {w: False for w in sorted_list}

    def print_round_letters(self):
        print("~~~~~~~" * 6)
        print("   ".join(self.letters))
        print("~~~~~~~" * 6)

    def print_round_anagrams(self):
        print("~~~~~~~" * 6)
        length = self.size
        for word in self.all_anagrams:
            text = word.upper() if self.all_anagrams[word] else BLANK_CHAR * len(word)
            if len(word) != length:
                length = len(word)
                print()
            print(text, end="  ")
        print("\n")
        # print(self.all_anagrams)

    def guess_word(self):
        guess = input("> ")
        if guess in ["q", "Q"]:
            return False
        elif guess in ["f", "F"]:
            if self.user.can_use_freebie():
                self.user.freebies -= 1
                self.give_word()
        elif guess in ["t", "T"]:
            if self.user.can_use_extra_time():
                self.user.extra_times -= 1
                # TODO
                # Give 30 more seconds of time
        elif guess in self.all_anagrams:
            self.all_anagrams[guess] = True
        return True

    def preguess_user_words(self):
        for word in self.all_anagrams:
            if self.user.has_word(word):
                self.all_anagrams[word] = True

    def give_word(self):
        for word in self.all_anagrams:
            if self.all_anagrams[word] is False:
                self.all_anagrams[word] = True
                return

    def is_round_won(self):
        return all(revealed for _, revealed in self.all_anagrams.items())
