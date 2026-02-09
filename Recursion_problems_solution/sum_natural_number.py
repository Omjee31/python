def sum_natural(n):
    # 1. Base Case: Stop when n is 0
    if n == 0:
        return 0
    
    # 2. Recursive Step: n + (sum of all numbers before n)
    return n + sum_natural(n - 1)

num = int(input("Enter Number: "))
result = sum_natural(num)
print(f"The sum is: {result}")
