# Import variance function from variance.py
import variance as var
import math

def std(values):
    # Get variance from variance module
    variance_value = var.variance(values)
    
    # Standard deviation = square root of variance
    std_value = math.sqrt(variance_value)
    
    return std_value

# Testing
print(f"Standard Deviation is equal to {std([23,45,67,89,12,34,56])}")
  
