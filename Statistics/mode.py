from collections import defaultdict

def mode(values):
    # Dictionary to store frequency of each value
    count = defaultdict(lambda: 0)
    
    # Count frequency of each element
    for s in values:
        count[s] += 1
    
    # Find maximum frequency
    max_count = max(count.values())
    
    # Collect all values having maximum frequency
    modes = [v for v in count if count[v] == max_count]
    
    return modes


values = [1,2,2,3,3]
result = mode(values)
print(result)
