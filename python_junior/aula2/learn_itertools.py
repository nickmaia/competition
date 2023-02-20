from itertools import combinations

print(combinations("ABCDEFGH", 2))
print(list(combinations("ABCDEFGH", 2)))

print(len(list(filter(lambda x: "A" in x, combinations("ABCDEFGH", 2)))))
