def is_palindrome(string):
    """
    Check if a string is a palindrome (reads same forwards and backwards).
    
    Args:
        string (str): Input string to check
        
    Returns:
        str: Message indicating if string is palindrome or not
    """
    # Clean and normalize the string: lowercase + remove non-alphabetic chars
    cleaned = ''.join(char.lower() for char in string if char.isalpha())
    
    # Compare cleaned string with its reverse
    if cleaned == cleaned[::-1]:
        return f'"{string}" IS a palindrome!'
    else:
        return f'"{string}" is NOT a palindrome.'

# Main execution block
if __name__ == "__main__":
    test_string = input("Enter string to check palindrome: ").strip()
    result = is_palindrome(test_string)
    print(result)
