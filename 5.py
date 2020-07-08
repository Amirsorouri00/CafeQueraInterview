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


def right(x):
    return x+1

def left(x):
    return x-1

def up(y):
    return y+1

def down(y):
    return y-1

def square(x):
    return x*x

def begin(level):
    if level == 0:
        return 0, 0
    else:
        return level, -(level)+1

def item(start, number, level, isList = False):
    minim = -(level)
    maxim = level
    x, y = begin(level)
    beg = [x,y]
    if isList == True:
        print(*beg, sep = " ")

    while number > start and beg[1] < maxim:
        beg[1] = up(beg[1])
        start+=1
        if isList == True:
            print(*beg, sep = " ")


    if number == start:
        return beg
    
    while number > start and beg[0] > minim:
        beg[0] = left(beg[0])
        start+=1
        if isList == True:
            print(*beg, sep = " ")

    if number == start:
        return beg
    
    while number > start and beg[1] > minim:
        beg[1] = down(beg[1])
        start+=1
        if isList == True:
            print(*beg, sep = " ")
        
    if number == start:
        return beg
    
    while number > start and beg[0] < maxim:
        beg[0] = right(beg[0])
        start+=1
        if isList == True:
            print(*beg, sep = " ")

    return beg

def calculate_level(number):
    level = 0
    temp = 0
    x = 1
    k = 2
    u = 1
    while temp + x < number:
        level+=1
        temp+=x
        x = (square(u+k) - temp)
        u+=2
    return level, temp, x

def get_item(number, isList = False):
    level, itemps_passd, items_in_level = calculate_level(number)
    return item(itemps_passd+1, number, level, isList)

def get_list(number):
    level, itemps_passd, items_in_level = calculate_level(number)
    temp = 0
    wnumber = 1
    while temp <= level and wnumber <= number:
        leve, passd, itemslev = calculate_level(wnumber)
        if temp == level:
            x = number
        else:
            x = passd + itemslev
        get_item(x, True)
        wnumber += itemslev
        temp+=1

def start():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(my_invr())
    for array in arr:
        if array[0] == 'list':
            get_list(int(array[1]))
        else:
            print(get_item(int(array[1]), False))

start()


