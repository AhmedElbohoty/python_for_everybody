fname = input("Enter file name: ")

try:
    handle = open(fname)
except:
    print(fname + ' file is not exist.')
    quit()

lst = list()

for line in handle:
    line = line.rstrip()
    words = line.split()

    for word in words:
        if word in lst:
            continue
        lst.append(word)

lst.sort()
print(lst)
