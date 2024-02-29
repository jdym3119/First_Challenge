'''This code defines a function `sums_nums(a)` that takes a list `a` as input. It initializes a global 
list variable `sums` and then iterates through the elements of the input list `a`.'''
def sums_nums(a):
    sums=[]
    # The line `for i in range(len(a)-1):` is setting up a loop that iterates through the indices of
    # the input list `a`, excluding the last index. The loop will run from 0 to `len(a)-2`, as
    # `range(len(a)-1)` generates a sequence of numbers starting from 0 up to `len(a)-2`.
    for i in range(len(a)-1):
        # The line `if i==0: sums.append(a[i]+a[i+1])` is a conditional statement within the loop.
        if i==0:sums.append(a[i]+a[i+1])
        # The line `elif a[i]+a[i+1]>=a[i]+a[i-1]: sums.append(a[i]+a[i+1])` is a conditional
        # statement within the loop.
        elif a[i]+a[i+1]>=a[i]+a[i-1]:sums.append(a[i]+a[i+1])
        # The line `else: sums.append(a[i]+a[i-1])` is part of an `else` block in the loop.
        else:sums.append(a[i]+a[i-1])
    # The line `return max(sums)` in the code snippet is returning the maximum value from the list
    # `sums`.
    return max(sums)
