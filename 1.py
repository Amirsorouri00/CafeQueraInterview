# Print the right input (capital, small is important)
# Be careful when popping from the list!!(it may be empty and you must check befor popping)
# You cannot pop from the str. you must use [:] for dropping some of the list


def validation (input):
    temp = []
    if len(input)%2 != 0:
        return False
    for elem in input:
        if elem in "{([":
            temp.append(elem)
            input = input[1:] 
        elif elem in "}])":
            if len(temp) == 0:
                return False
            el = temp.pop()
            if (elem == ")" and el == "(" or elem == "}" and
                el == "{" or elem == "]" and el == "[") == False:
               return False 
            else:
                input = input[1:]
        else: 
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