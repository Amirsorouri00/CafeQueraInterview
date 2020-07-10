def getword(string, size):
    seen = -1
    for i in range(0, size - 1):
        word = ""
        if string[i] == "<":
            seen = 1
            return 1, size, word, string
            # return -1, size, word
        elif string[i] == ">":
            return -1, size, word, string
        else:
            word += string[i]
        string = string[1:]
        size-=1
    return -1, size, word, string
    # return 1, size, word

def starttag(string, size):
    # size = len(string)
    seen = -1
    tag = ""
    for i in range(0, size):
        if string[i] != ">":
            tag+=string[i]
        else:
            seen = 1
            break
        string = string[1:]
        i = 0    
        size-=1

    if tag == "down" and seen == 1:
        valid, size, word, string= getword(string, size)
        if valid == -1:
            return -1, 0, "0"
        stack.append["d%/{0}".format(word)]
        tagstack.append["d"]
        
        valid, size, string = endtag(string, size)
        if valid == -1:
            return -1, 0, "0"
        return 1, size, string

    elif tag == "up" and seen == 1:
        valid, size, word, string = getword(string, size)
        if valid == -1:
            return -1, 0, "0"
        stack.append["u%/{0}".format(word)]
        tagstack.append("u")

        valid, size, string = endtag(string, size)
        if valid == -1:
            return -1, 0, "0"
        return 1, size, string
    else:
        return -1, 0, "0"

def endtag(string, size):
    seen = -1
    if len(tagstack) == 0:
        return -1, 0, "0"

    for i in range(0, size):
        tag = ""
        if string[i] != ">":
            tag+=string[i]
        else:
            seen = 1
        string = string[1:]
        i = 0    
        size-=1
    if tag == "down" and seen == 1:
        if tagstack[-1] != "d":
            return -1, 0, "0"
        tagstack.pop()
        return 1, size, string
    elif tag == "up" and seen == 1:
        tagstack.pop()
        return 1, size, string
    else:
        return -1, 0, "0"


def main(htmstr, size):
    
    string = htmstr
    lasttagstart = False
    lasttagdown = False
    final = []
    for i in range(0, size):
        if string[i] == "<":
            # start or end tag
            string = string[1:]
            size-=1
            if i == size - 1:
                return False
            else:
                if string[i+1] == "/":# and/or len(tagstack) == 0:
                    #end tag
                    print("Invalid")
                    return
                    # string = string[1:]
                    # size-=1
                    # valid, size, string = starttag(string, size)
                else:
                    #start tag
                    valid, size, string = starttag(string, size)
                    if valid == -1:
                        print("Invalid")
                        return
                    final.append("r%/")
        else:
            valid, size, word, string = getword(string, size)
            final.append(word)
    finalstring = ""
    for s in final:
        if len(s) == 3 and s[0] == "r" and s[1] == "%" and s[2] == "/":
            # s = s[3:]
            word = stack.pop(0)
            if word[0] == "d":
                word = word[3:]
                word = word.lower()
            if word[0] == "u":
                word = word[3:]
                word = word.upper()
            finalstring+= word
        else:
            finalstring+= s
    print("Valid")
    print(finalstring)
