# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase and remove spaces for accurate checking
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Driver code
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')