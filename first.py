# print(type(4))
# print(type("python"))
# print(type(4.0))

# print(int(4.0) + 1)
# print(float(8))
# print(9 / 2)

""" string = "123"
print(float(string) + 1) """


""" inp = input("What is your name?")
print("Hello", inp) """

""" x = 5

if x < 6:
    print("Smaller")
elif x < 10:
    print("Medium")
else:
    print("Bigger") """


""" string = "Hello"
# string = "44"

try:
    istr = int(string)
except:
    istr = -1

print(istr) """

""" n = 4
while n < 9:
    print(n)
    n = n + 1 """

""" while True:
    line = input("> ")
    if line[0] == "#":
        print("Don't print")
        continue
    if line == "done":
        break
    print(line) """


""" def largest(numbers):
    largest = -1
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(largest([45, 1, 890, 142, 4, 17, 6]))
print(largest([45, 1, 8, 42, 4, 17, 6])) """


def smallest(numbers):
    smallest = None
    for number in numbers:
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number
    return smallest


print(smallest([45, 0, 890, 142, 4, 17, 6]))
print(smallest([45, 2, -8, 42, 4, 17, 6]))

""" numbers = [14, 5, 99, 77, 13]

found = False
for i in numbers:
    if i == 14:
        found = True
        break
    print(i)

print(found) """
