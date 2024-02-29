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
    # The line `if z == '+': return x + y` in the `basic_math_operations` function is checking if the
    # value of the parameter `z` is equal to the symbol '+'. If this condition is true, it means that
    # the function should perform addition between the numbers `x` and `y`.
    if z=='+':return x+y
    # The line `elif z=='-': return x-y` in the `basic_math_operations` function is checking if the
    # value of the parameter `z` is equal to the symbol '-'. If this condition is true, it means that
    # the function should perform subtraction between the numbers `x` and `y`. In other words, when
    # `z` is '-', the function will subtract `y` from `x` and return the result.
    elif z=='-':return x-y
    # The line `elif z=='*': return x*y` in the `basic_math_operations` function is checking if the
    # value of the parameter `z` is equal to the symbol '*'. If this condition is true, it means that
    # the function should perform multiplication between the numbers `x` and `y`. In other words, when
    # `z` is '*', the function will multiply `x` by `y` and return the result.
    elif z=='*':return x*y
    # The code snippet `elif z=='/': if y!=0: return x/y else: return "It\'s impossible."` is handling the
    # division operation in the `basic_math_operations` function.
    elif z=='/':
        if y!=0: return x/y
        else: return "It\'s impossible."
