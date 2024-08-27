def check_positive_number(num):

    num = int(input("Enter any value :"))

    if num < 0:
        raise ValueError("The number must be positive!")
    return num

# Example usage
try:
    check_positive_number(int) 
    print("Input is positive")

except Exception as e:
 # This block catches any other unexpected exceptions and prints the error message
    print(e)