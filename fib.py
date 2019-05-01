## Print i number of Fibonacci numbers

## variables for Fibonacci calculations are x, y, and z
## i = number of Fibonacci numbers to print

def fibonacci(i):
    x = 1
    print(x)
    y = 1
    print(y)
    i = i-2 # to account for x and y starting values
    while i > 0:
        z = x + y
        print(z)
        i = i - 1

        if i > 0:
            x = y + z
            print(x)
            i = i - 1
        else:
            return
        
        if i > 0:
            y = z + x
            print(y)
            i = i - 1
        else: 
            return

fibonacci(10)
