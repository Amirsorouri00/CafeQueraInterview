def validation (input):
    temp = []
    if len(input)%2 != 0:
        return False
    if input[0] in "}])":
        return False
    for elem in input:
        if elem in "{([":
            temp.append(elem)
            input = input[1:] 
        elif elem in "}])":
            if len(temp) == 0:
                return False
            el = temp.pop()
            if el == "(" and elem != ")":
                return False
            elif el == "{" and elem != "}":
                return False
            elif el == "[" and elem != "]":
                return False
        else: 
            return False
    if len(temp) != 0:
        return False
    return True

def start():
    i = input()
    o = validation(i)
    if o == True:
        print("Valid")
    else:
        print("Invalid")

start()
