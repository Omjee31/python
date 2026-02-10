def fibo(num):
    # Initialize the first two Fibonacci numbers
    # 'first' represents the previous value
    # 'second' represents the next value
    first, second = 0, 1
    
    # Loop 'num' times to generate Fibonacci numbers
    for i in range(num):
        # Print the current Fibonacci number
        print(first, end=" ")
        
        # Update values using tuple assignment
        # RHS is evaluated first, so no value is lost
        # New first  = old second
        # New second = old first + old second
        first, second = second, first + second

    # Function does not return anything explicitly
    # By default, Python returns None


    '''
    ❌ Incorrect approach (commented out)
    These lines overwrite 'first' before computing 'second',
    which breaks Fibonacci logic.
    
    first = second
    second = first + second
    '''
    

if __name__ == "__main__":
    # Take input from user for number of terms
    num = int(input("Enter Number : "))
    
    # Call the function to print Fibonacci series
    # fibo(num) prints the series but returns None
    print(fibo(num))



