def validateInput(inp, type=int):
    """
    Function to validate the input

    Args:
        inp ( Any given from the input() method ): Input string
        type ( must be in (int, float, str) ): Type of input
    """
    try:
        fn = type
        if type == int:
            fn = int
        elif type == float:
            fn = float
        else:
            fn = str
        return fn(inp)
    except ValueError:
        raise ValueError("Input is not purely the type of {}".format(type))


def countStrictDecreasingSubArrays(arr):
    """
    Function to count the total number of strictly decreasing sublists in an array

    Args:
        arr (list): List of integers
    """
    count = 0
    if len(arr) == 0:
        return count

    length = 1
    for i in range(1, len(arr)):
        if (arr[i - 1] > arr[i]):
            length += 1
        else:
            count += (((length - 1) * length) // 2)
            length = 1

    if (length > 1):
        count += (((length - 1) * length) // 2)
    return count


try:
    arrLen = validateInput(input())
    arr = []
    if arrLen != 0:
        arr = input().split(' ')

    if arrLen != len(arr):
        raise ValueError(
            "Number of elements is not equal to the number of entries")

    # validate type of items given from the input
    [validateInput(x) for x in arr]

    result = countStrictDecreasingSubArrays(arr)
    print(result)
except Exception as e:
    raise ValueError(e)
