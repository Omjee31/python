#This Code is To Find Occurances Of Target From Main list 
import random  # Importing random module

# Function to search target in list
def find(to_search, target):
    # Loop through list with index and value
    for i, value in enumerate(to_search):
        
        # Compare both words in lowercase (case-insensitive search)
        if value.lower() == target.lower():
            return f"{target} At Index {i}"  # Return index if found
    
    # If loop finishes and no match found
    return f"{target} Not Found"


# Sample list
list1 = ['Words', 'Spealing', 'Meaning', 'letter', 'Charecter']

# Randomly select one word from list
target = random.choice(list1)

# Call function and print result
print(find(list1, target))
