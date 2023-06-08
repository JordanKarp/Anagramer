class User:
    def __init__(self, name):
        self.name = name
        self.vocab = {num: set() for num in range(2, 16)}

    @property
    def words_known(self):
        return sum(len(values) for values in self.vocab.values())

    @property
    def words_known_value(self):
        return sum(len(values) * key for key, values in self.vocab.items())

    def has_word(self, word):
        return word in self.vocab[len(word)]

    def add_word(self, word):
        length = len(word)
        if word not in self.vocab[(length)]:
            self.vocab[length].add(word)

    def print_vocab(self):
        print("Words Collected:")
        for k, v in self.vocab.items():
            print(f'{k}: {", ".join(sorted(v))}')
