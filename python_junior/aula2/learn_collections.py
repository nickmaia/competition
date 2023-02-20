from collections import Counter

c = Counter('abcdeabcdabcaba')

print(c)

print(c['a'])
print(c['x'])

print(c.most_common(1))

print(c.most_common(1)[0][0])