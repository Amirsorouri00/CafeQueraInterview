tagstack = []
donestack = []
def reverse(string):
    i = 0
    replaced = 0
    if len(string) == 0:
        return 1, '', i
    else:
        tempstr = ''
        while i < len(string):
            # print("i:", i)
            entered = False
            if string[i] == "<":
                # print("<: ", i, len(string), string)
                i+=1
                if i + 6 <= len(string):                
                    entered = True
                    k=i
                    d = i
                    st = string[i:i+6]
                    # print("st:", st)
                    if st == "/down>":
                        # i+=6
                        d+=6
                        tag = tagstack.pop()
                        if tag != "d":
                            return -1, "0", -1
                        return 1, tempstr, d + replaced
                if i + 5 <= len(string):
                    entered = True
                    k=i
                    d = i
                    st = string[i:i+5]
                    # print("st:", st)
                    if st == "down>":
                        # print("down>")
                        d+=5
                        tagstack.append('d')
                        valid, resstr, resi = reverse(string[d:])
                        string = string.replace(string[i-1:resi+d], '')
                        replaced += (len(string[i-1:resi+d]))
                        if valid == -1:
                            return -1, "0", -1
                        if i >= len(string):
                            tempstr+= resstr.lower() 
                        else:
                            tempstr+= "r%/"
                            donestack.append(resstr.lower())
                if i + 4 <= len(string):
                    entered = True
                    k=i
                    d = i
                    st = string[i:i+4]
                    if st == "/up>":
                        # print("/up>")
                        d+=4
                        tag = tagstack.pop()
                        if tag != "u":
                            return -1, "0", -1
                        return 1, tempstr, d + replaced
                if i + 3 <= len(string):
                    entered = True
                    k=i
                    d = i
                    st = string[i:i+3]
                    # print("st:", st)
                    if st == "up>":
                        d+=3
                        # print(string, i, d, string[d:])
                        tagstack.append('u')
                        valid, resstr, resi = reverse(string[d:])
                        string = string.replace(string[i-1:resi+d], ' ')
                        replaced += (len(string[i-1:resi+d]))
                        if valid == -1:
                            return -1, "0", -1
                        if i >= len(string):
                            tempstr+= resstr.upper()
                        else:
                            tempstr+= "r%/"
                            donestack.append(resstr.upper())
                        # print(resstr.upper())
                if entered == False:
                    # print("invalidddd", k)
                    return -1, "0", -1
            else:
                # print("word", string[i])
                tempstr += string[i]
                i+=1
        return 1, tempstr, i


def start():
    inp = input()
    valid, finalstr, resindex = reverse(inp)
    # print(finalstr)
    ind = finalstr.find("r%/")
    while ind != -1:
        finalstr = finalstr[:ind] + donestack.pop(0) + finalstr[ind+3:]
        ind = finalstr.find("r%/")

    if valid == -1:
        print("Invalid")
    else:
        print("Valid")
        print(finalstr)

start()