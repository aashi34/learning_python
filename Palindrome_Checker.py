## Create a palindrome checker in Python
n = input("Enter a string to check if it's a palindrome: ")
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Test the function
# test_string = "A man, a plan, a canal: Panama"
test_string = n
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")

