class User:
    def __init__(self, name):
        self.name = name
        self.vocab = {num: set() for num in range(2, 16)}
        self.points = 0
        self.freebies = 1
        self.extra_times = 1
        self.extra_lives = 0

    @property
    def words_known(self):
        return sum(len(values) for values in self.vocab.values())

    @property
    def words_known_value(self):
        return sum(len(values) * key for key, values in self.vocab.items())

    def can_use_freebie(self):
        return self.freebies >= 1

    def can_use_extra_time(self):
        return self.extra_times >= 1

    def can_use_extra_life(self):
        return self.extra_lives >= 1

    def use_freebie(self):
        if self.freebies < 1:
            return False
        self.freebies -= 1
        return True

    def has_word(self, word):
        return word in self.vocab[len(word)]

    def add_word(self, word):
        length = len(word)
        if word not in self.vocab[(length)]:
            self.vocab[length].add(word)
            self.points += length

    def print_vocab(self):
        print("Words Collected:")
        for k, v in self.vocab.items():
            print(f'{k}: {", ".join(sorted(v))}')
