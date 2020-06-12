name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print('File cannot be opened:', name)
    exit()

emails = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

largest = -1
sender = None
for key, value in emails.items():
    if value > largest:
        largest = emails[key]
        sender = key

print(sender, largest)
