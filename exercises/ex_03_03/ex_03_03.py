score_input = input("Enter Score: ")

try:
    score = float(score_input)
except:
    print("Please enter a valid number")
    quit()

if score > 1.0:
    print("The score range must be between 0 and 1")
elif score < 0.0:
    print("The score range must be between 0 and 1")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
