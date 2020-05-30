# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fhandle = open('./files/' + fname)
except:
    print('File cannot be opened:', fname)
    quit()

total = 0
count = 0

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sppos = line.find(' ')
    number = line[sppos:].lstrip()

    count = count + 1
    total = total + float(number)

average = total/count

print('Average spam confidence:', average)
