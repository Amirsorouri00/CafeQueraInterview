# type must be in (int, float, str)
def validate_input(inp, type=int):
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


try:
    R = validate_input(input())
    C = validate_input(input())

    matrix = []

    for i in range(0, R):
        row = input().split(' ')
        if C != len(row):
            raise ValueError(
                "Number of columns is not equal to the number of entries")
        [validate_input(x) for x in row]
        matrix.append(row)
    print(matrix)

except Exception as e:
    raise ValueError(e)


def countStrictDecreasingSubArrays(arr, arrLen):
    cnt = 0
    if arrLen == 0:
        return cnt

    # Initialize length of current
    # decreasing subarray
    len = 1

    # Traverse through the array
    for i in range(arrLen - 1):

        # If arr[i+1] is less than arr[i],
        # then increment length
        if (arr[i + 1] < arr[i]):
            len += 1

        # Else Update count and
        # reset length
        else:
            cnt += (((len - 1) * len) // 2)
            len = 1

    # If last length is more than 1
    if (len > 1):
        cnt += (((len - 1) * len) // 2)

    return cnt


# Function to calculate the score
# of the parentheses using stack
# https://leetcode.com/problems/score-of-parentheses/solution/
def scoreOfParenthesesCalculator(expression):
    stack = [0]
    for c in expression:
        if c == '(':
            stack.append(0)
        else:
            val = stack.pop()
            stack[-1] += max(2 * val, 1)

    return stack.pop()

    # a = [1, 2, 1, 0, 2, 1, 6, 4, 2]
    # b = [2, 4, 6, 7]
    # c = [5, 5, 2, 4, 6, 7]
    # l1 = len(a)
    # l2 = len(b)
    # l3 = len(c)
