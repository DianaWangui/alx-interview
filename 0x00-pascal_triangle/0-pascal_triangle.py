#!/usr/bin/python3
"""
A Python module that prints the
Pascal's Triangle based on the number
it is called with.
This is an attempt to solve an #ALX_SE interview question

I'll come back to this question to see if
it can be solved using recursion
"""


def pascal_triangle(n):
    """
    A function that returns a list of list of integers
    representing the Pascal's triangle of n

    Arguments:
        n: Integer, the number of lists that the function returns

    Return:
        - A list of lists of integers if n is a valid number
        - An empty list if n is less than or equal to zero
    """
    # The list of lists that will be appended to, must be initialized to 1
    finalArray = [[1]]
    if n <= 0:
        return []
    elif not isinstance(n, int):
        return False
    else:
        for i in range(n - 1):
            # This temporary array is used to access
            # the value of the last index of finalArray
            # It stores [0, valueOfLastIndex, 0]
            temp = [0] + finalArray[-1] + [0]
            # An empty array that will always be used to append to
            emptyArray = []
            for j in range(len(finalArray[-1]) + 1):
                # This is where the magic of appending the two previous
                # numbers above it works
                emptyArray.append(temp[j] + temp[j + 1])
            # print(emptyArray)
            finalArray.append(emptyArray)
        return finalArray
