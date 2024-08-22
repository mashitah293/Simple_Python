# Get user input for a number
number = int(input("Enter a number: "))

# Display the entered number
print("You entered:", number)

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero.")
