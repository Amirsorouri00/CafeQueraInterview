tests = [
    #'2 ^ ( 1 + 3 ^ 2 )',
    #'( 3 * 5 ) - ( 1 > 2 > 3 < 4 )',
    #'4 ^ ( 10 < 2 ) / 5 + 100',
    '( 2 + 3 )',
    '( 2 + 3 ) * ( 7 + 12 )',
    '( 2 + 3 ) * ( ( 7 + 12 ) + ( 3 * ( 1 + 2 ) ) )'
]

expected = [
    #1024,
    #12,
    #103,
    #140
    5,
    95,
    140
]

def expr_eval(s):
    # print("EXPR:", s)
    tokens = s.split()
    output_stk = []
    operator_stk = []

    precedence = {
        '(': 0,
        '+':1, '-':1, '<':1, '>':1,
        '*':2, '/':2,
        '^':3,
    }

    for t in tokens:
        if t.isdigit():
            output_stk.append(int(t))
            continue
        elif t == '(':
            operator_stk.append(t)
            continue
        elif t == ')':
            while operator_stk:
                op = operator_stk.pop()
                if op == '(':
                    break

                b = output_stk.pop()
                a = output_stk.pop()
                if op == '-': output_stk.append(a - b)
                elif op == '+': output_stk.append(a + b)
                elif op == '<': output_stk.append(1 if a < b else 0)
                elif op == '>': output_stk.append(1 if a > b else 0)
                elif op == '*': output_stk.append(a * b)
                elif op == '/': output_stk.append(a // b)
                elif op == '^': output_stk.append(a ** b)
                else:
                    raise Exception("Unknown operator: %s" % op)
            continue

        prec_t = precedence[t]
        while operator_stk and prec_t <= precedence[operator_stk[-1]]:
            op = operator_stk.pop()
            b = output_stk.pop()
            a = output_stk.pop() # 'a' went on first!
            if op == '-': output_stk.append(a - b)
            elif op == '+': output_stk.append(a + b)
            elif op == '<': output_stk.append(1 if a < b else 0)
            elif op == '>': output_stk.append(1 if a > b else 0)
            elif op == '*': output_stk.append(a * b)
            elif op == '/': output_stk.append(a // b)
            elif op == '^': output_stk.append(a ** b)
            else:
                raise Exception("Unknown operator: %s" % op)
        operator_stk.append(t)


    while operator_stk:
        op = operator_stk.pop()
        if op == '(':
            raise Exception('Mismatched opening parenthesis!')

        b = output_stk.pop()
        a = output_stk.pop() # 'a' went on first!
        if op == '-':   output_stk.append(a - b)
        elif op == '+': output_stk.append(a + b)
        elif op == '<': output_stk.append(1 if a < b else 0)
        elif op == '>': output_stk.append(1 if a > b else 0)
        elif op == '*': output_stk.append(a * b)
        elif op == '/': output_stk.append(a // b)
        elif op == '^': output_stk.append(a ** b)
        else:
            raise Exception("Unknown operator: %s" % op)

    return output_stk.pop()


def start():
    expr = input()
    i = 0
    last_digit = False
    digit = ''
    spaced_expr = ''
    while i < len(expr):
        if expr[i].isdigit() == True:
            last_digit = True
            # i+=1
            digit+=expr[i]
            i+=1
            # continue
        else:
            if last_digit == True:
                spaced_expr+= digit + " "
                last_digit = False
                digit = ''
            spaced_expr += expr[i] + " "
            i+=1

    r = expr_eval(spaced_expr)
    print(r)

start()