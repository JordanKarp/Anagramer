from game_state import load_words


WORD_FILE = "wordList.txt"

words = load_words(WORD_FILE)

count_dict = {}

for word in words:
    if len(word) in count_dict:
        count_dict[len(word)] += 1
    else:
        count_dict[len(word)] = 1

li = sorted(count_dict.items())
print(li)
total = 0
for k, v in dict(li).items():
    if k <= 15:
        total += k * v
        print(f"{k}:\t {v}")

print(total)