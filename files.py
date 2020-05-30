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
fname = input('Enter the file name: ')
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

print('There were', count, 'subject lines in', fname)
