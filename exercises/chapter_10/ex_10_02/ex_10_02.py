fname = input("Enter a file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    handle = open(fname)
except:
    print('No File with this name')
    exit()


lines = [line.split()[5] for line in handle if line.startswith('From')
         and len(line.split()) > 6]

counts = dict()
for time in lines:
    time = time.split(':')
    hour = time[0]
    counts[hour] = counts.get(hour, 0) + 1

sorted_hours = sorted(counts.items())

for k, v in sorted_hours:
    print(k, v)
