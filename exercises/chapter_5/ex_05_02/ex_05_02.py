largest = None
smallest = None

while True:
    num_input = input("Enter a number: ")

    if num_input == "done":
        break

    try:
        num = int(num_input)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
        smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)
