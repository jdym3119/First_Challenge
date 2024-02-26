def strings(x):
    """
    The function takes a list of strings as input and returns a list of strings that have the same
    characters in any order.
    :param x: The function `strings` takes a list of strings as input and returns a list of strings
    where each pair of strings have the same set of characters. The code then prompts the user to enter
    a list of strings, calls the `strings` function with the input list, and prints the result
    :return: The function `strings(x)` takes a list of strings as input, compares each pair of strings
    to see if they have the same set of characters, and returns a list of unique strings that have at
    least one other string with the same set of characters.
    """
    b=[]
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if set(x[i])==set(x[j]) and x[j] not in b:
                b.append(x[i])
                b.append(x[j])
    return list(set(b))    