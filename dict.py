""" room = dict()
room['chair'] = 'red'

print(room)
print(room['chair']) """

""" bag = {'a': 1, 'b': 3}
print(bag) """

letters = ['a', 'f', 'c', 'c', 'a', 'b', 'c', 'c']
counts = dict()


""" for letter in letters:
    if letter not in counts:
        counts[letter] = 1
        continue
    counts[letter] = counts[letter] + 1 """

for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

keys = counts.keys()  # Iterable but not indixable
values = counts.values()
items = counts.items()

""" print(counts)
print(keys)
for a in keys:
    print(a) """

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word


#print(bigWord, bigCount)
