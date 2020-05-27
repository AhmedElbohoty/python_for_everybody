hours_inp = input("Enter Hours: ")
rate_inp = input("Enter Rate: ")

try:
    hours = float(hours_inp)
    rate = float(rate_inp)
except:
    print("Error, please enter numeric input")
    quit()


def compute_pay(hours, rate):
    if hours <= 40:
        total = hours * rate
    else:
        reg_hours = 40 * rate
        extra_hours = (hours - 40) * rate * 1.5
        total = reg_hours + extra_hours

    return total


total = compute_pay(hours, rate)


print("Pay", total)
