def tagChecker(start, finish):
    if start == "<d>":
        return 1
    elif finish == "</d>":
        return 2
    elif start == "<u>":
        return 3
    elif finish == "</u>":
        return 4
    else: 
        print("invalidated")
        return -1

stackOp = []
strStack = []
def validator(str):
    i = 0
    while i < len(str):
        if str[i] == "<":
            res = tagChecker(str[i:i+3], str[i:i+4])
            if res == -1:
                return -1
            else:
                if res == 1 or res == 3:
                    i+=3
                    if res == 1:
                        stackOp.append("<d>")
                    elif res == 3:
                        stackOp.append("<u>")
                else: 
                    i+=4
                    op = ""
                    strTmp = "<"
                    seen = False
                    while op not in ["<d>", "<u>"] and len(stackOp) > 0:
                        op = stackOp.pop()
                        if op in ["<d>", "<u>"]:
                            seen = True
                            break
                        elif op[0] == "<":
                            strStack.append(op)
                            strTmp+=">"
                        else:
                            strTmp+=op
                    if res == 2 and seen:
                        if op != "<d>":
                            return -1
                        else:
                            tmp = strTmp.lower()
                            stackOp.append(tmp)
                    elif res == 4 and seen:
                        if op != "<u>":
                            return -1
                        else:
                            tmp = strTmp.upper()
                            stackOp.append(tmp)
                    elif seen != True:
                        return -1
        else:
            stackOp.append(str[i])
            i+=1
            continue
    return 1

def start(str):
    resp = validator(str)
    if resp == -1:
        print("Invalid")
        return 
    str = ""
    for st in stackOp:
        str+=st[::-1]
    result = ""
    for s in str:
        if s == ">":
            result+=strStack.pop()[1:]
        elif s == "<":
            continue
        else:
            result+=s
    print("Valid")
    print(result)

str = input()
str = str.replace("<down>", "<d>").replace("</down>", "</d>").replace("<up>", "<u>").replace("</up>", "</u>")
start(str)
