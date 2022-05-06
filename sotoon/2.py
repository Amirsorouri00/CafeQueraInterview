def scoreOfParenthesesCalculator(expression):
    """
    Function to calculate the score of expression 
    consisting balanced parantheses

    Args: 
        expression (str): String of balanced parantheses
    """
    res = bal = 0
    for i, c in enumerate(expression):
        if c == '(':
            bal += 1
        else:
            bal -= 1
            if expression[i-1] == '(':
                res += 1 << bal
    return res


def isBalanced(expression):
    brackets = ['()']
    while any(x in expression for x in brackets):
        for br in brackets:
            expression = expression.replace(br, '')
    return not expression


INPUT_EXAMPLE = "()(((()())())())"  # SCORE = 23
CONSTANT = 2021
try:
    expression = input()
    if not isBalanced(expression):
        raise ValueError("Expression is not balanced")

    result = scoreOfParenthesesCalculator(expression)
    print(result % CONSTANT)
except Exception as e:
    raise ValueError(e)
