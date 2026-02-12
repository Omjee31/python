"""
Program: Character Frequency Counter
Author: Omjee Singh
Description:
    This program takes a string input from the user
    and counts the frequency of each character.
    The counting is case-insensitive.
"""

def count_character_frequency(text: str) -> dict:
    """
    Count frequency of each character in a given string.

    Parameters:
        text (str): Input string

    Returns:
        dict: Dictionary containing character frequencies
    """

    # Create an empty dictionary to store frequencies
    frequency = {}

    # Convert text to lowercase to make counting case-insensitive
    for char in text.lower():

        # If character exists, increment count
        # Otherwise initialize with 1
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


# ===== Main Program Execution =====
if __name__ == "__main__":

    # Take input from user
    user_input = input("Enter a string: ")

    # Call the function
    result = count_character_frequency(user_input.strip())

    # Print the result
    print("\nCharacter Frequencies:")
    for char, freq in result.items():
        print(f"'{char}': {freq}")
