""" fhandle = open("./files/mbox-short.txt", 'r')
count = 0 """


""" for line in fhandle:
    count = count + 1
print('Line count:', count) """

""" inp = fhandle.read()
print('Length:', len(inp))
print(len(inp.split('\n'))) """

""" for line in fhandle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line) """


""" for line in fhandle:
    line = line.rstrip()
    if not '@uct' in line:
        continue
    print(line) """

# ============================================= #
"""fname = input('Enter the file name: ')
try:
    fhandle = open('./files/' + fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0

 for line in fhandle:
    if not line.startswith('Subject:'):
        continue
    count = count + 1

print('There were', count, 'subject lines in', fname) """

handle = open('./files/mbox-short.txt')

"""for line in handle:
    line = line.rstrip()
    words = line.split()

    if len(words) < 3 or words[0] != 'From':
        continue

    print(words[2]) """

lines = [line.rstrip() for line in handle if line.startswith('From')]
print(lines)
