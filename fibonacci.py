# def factorial(n):
   
#     # Base case: 0! and 1! are both 1
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Outputs: 120

def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)
print(fabonacci(5))
