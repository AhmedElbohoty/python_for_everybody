fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    handle = open(fname)
except:
    print(fname + ' file is not exist.')
    quit()

handle = open(fname)
count = 0

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])


print("There were", count, "lines in the file with From as the first word")
