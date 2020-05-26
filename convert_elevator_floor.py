# Convert elevator floor
inp = input("Europe floor?")

try:
    usf = int(inp) + 1
except:
    usf = -1

if usf < 0:
    print("Not a Number")
else:
    print('US Floor', usf)
