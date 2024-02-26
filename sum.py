'''This code defines a function `sums_nums(a)` that takes a list `a` as input. It initializes a global 
list variable `sums` and then iterates through the elements of the input list `a`.'''
def sums_nums(a):
    sums=[]
    for i in range(len(a)-1):
        if i==0:sums.append(a[i]+a[i+1])
        elif a[i]+a[i+1]>=a[i]+a[i-1]:sums.append(a[i]+a[i+1])
        else:sums.append(a[i]+a[i-1])
    return max(sums)