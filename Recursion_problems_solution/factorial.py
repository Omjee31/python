def factorial_Recursion(n):
    """Compute factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_Recursion(n - 1)


# Interactive demo
if __name__ == "__main__":
    num = int(input("Enter The Number You Want That Factorial: "))
    print(f"Factorial Of {num} Using Recursion: {factorial_R
