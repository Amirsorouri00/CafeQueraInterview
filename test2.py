import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return list(map(int,input().split()))
def my_invr():
    return list(input().split())


def start():
    label = input()
    red = 0
    yellow = 0
    nakhor = False
    noGreen = False
    for c in label:
        if red >= 3:
            nakhor = True
            break
        elif red >= 2 and yellow >=2:
            nakhor = True
            break
        else:
            if c == 'R':
                red+=1
            elif c == "Y":
                yellow+=1
            else:
                noGreen = True
    
    if nakhor or noGreen == False:
        print("nakhor lite")
    else:
        print("rahat baash")


start()
