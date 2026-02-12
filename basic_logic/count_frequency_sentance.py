"""
Program: Word Frequency Counter
Author: Omjee Singh
Description:
    This program takes a sentence as input
    and counts the frequency of each word.
    The counting is case-insensitive.
"""

def count_word_frequency(sentence: str) -> dict:
    """
    Count frequency of each word in a given sentence.

    Parameters:
        sentence (str): Input sentence

    Returns:
        dict: Dictionary containing word frequencies
    """

    # Convert sentence to lowercase (case-insensitive counting)
    sentence = sentence.lower()

    # Split sentence into words
    words = sentence.split()

    # Create empty dictionary to store word frequencies
    frequency = {}

    # Count occurrences of each word
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# ===== Main Program Execution =====
if __name__ == "__main__":

    # Take input from user
    user_input = input("Enter a sentence: ")

    # Call the function
    result = count_word_frequency(user_input)

    # Print result
    print("\nWord Frequencies:")
    print(result)
