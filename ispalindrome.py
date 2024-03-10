import re
def isPalindrome(s):
    # Remove spaces, numbers, and special characters using regular expression
    cleaned_string = re.sub(r'[^a-zA-Z]', '', s)
    
    # Convert the string to lowercase for case-insensitive comparison
    cleaned_string = cleaned_string.lower()
    
    # Check if the cleaned string is a palindrome
    return cleaned_string == cleaned_string[::-1]

# Example usage:
input_str = "A man, a plan, a canal, Panama!"
result = isPalindrome(input_str)

print(result)