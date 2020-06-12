letters = ['a', 'f', 'c', 'c', 'a', 'b', 'c', 'c']
counts = dict()

for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

tup = sorted(counts.items())
print(tup)

lis = list()

for k, v in counts.items():
    lis.append((v, k))

tup_by_value = sorted(lis, reverse=True)
print(tup_by_value)


""" (a, b) = (1, 2)
print(a) """
