# 0.408s
# 0.286s
from collections import Counter
from string import ascii_lowercase
from sys import stdin

num_cases = int(stdin.readline())

for _ in range(num_cases):

    text = stdin.readline().lower()
    text = "".join([letra for letra in text if letra in ascii_lowercase])
    x = Counter(text)
    freq_max = x.most_common(1)[0][1]
    letters = ""
    for key in x:
        if x[key] == freq_max:
            letters += key
    print("".join(sorted(letters)))