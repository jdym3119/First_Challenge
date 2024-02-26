def basic_math_operations(x,y,z):
    """
    The function `basic_math_operations` takes three inputs (x, y, z) and performs basic arithmetic
    operations (+, -, *, /) based on the value of z.
    
    :param x: The parameter `x` represents the first number in the operation
    :param y: The parameter `y` in the `basic_math_operations` function is the second number that you
    input when calling the function. It is the second operand for the mathematical operation specified
    by the third parameter `z`
    :param z: The parameter `z` in the `basic_math_operations` function represents the mathematical
    operation to be performed on the numbers `x` and `y`. It can be one of the following symbols: '+',
    '-', '*', or '/'
    :return: The function `basic_math_operations` takes three parameters `x`, `y`, and `z`. It performs
    a basic mathematical operation based on the value of `z` and returns the result.
    """
    if z=='+':return x+y
    elif z=='-':return x-y
    elif z=='*':return x*y
    elif z=='/':return x/y