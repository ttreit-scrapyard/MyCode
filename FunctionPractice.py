# Understanding functions
# A function is called and returns something.
# the 'something' it returns replaces the function() from where it was called.
# so print(function1()) becomes print(return_value_of_fucntion1)

def add(num1, num2):
    # Add two numbers and return sum
    z = num1 + num2
    return z

def main():
    print(add(1, 1)) # return from function add replaces add(1, 1) with 2. print(2)
    print(add(1, 5)) # becomes print(6)
    print(add(1, 154)) # becomes print(154)

main()