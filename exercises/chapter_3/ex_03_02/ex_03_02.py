hours_inp = input("Enter Hours: ")
rate_inp = input("Enter Rate: ")

try:
    hours = float(hours_inp)
    rate = float(rate_inp)
except:
    print("Error, please enter numeric input")
    quit()

if hours <= 40:
    total = hours * rate
else:
    reg_hours = 40 * rate
    extra_hours = (hours - 40) * rate * 1.5
    total = reg_hours + extra_hours

print(total)
