# Import mean function from mean.py file
import mean as m

def variance(values):
    # Calculate mean using external mean file
    avg = m.meann(values)
    
    # Apply variance formula:
    # (value - mean)^2 for each value
    # Sum them and divide by total number of elements
    var = sum((v - avg) ** 2 for v in values) / len(values)
    
    return var

# Testing the function
print(f"Variance is equal to {variance([23,45,67,89,12,34,56])}")
