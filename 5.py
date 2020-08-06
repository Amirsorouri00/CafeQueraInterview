import math

def right(x):                      
    return x+1                     
                                   
def left(x):                       
    return x-1                     
                                   
def up(y):                         
    return y+1                     
                                   
def down(y):                       
    return y-1                     
                                   
def begin(level):                  
    if level == 0:                 
        return 0, 0                
    else:                          
        return level, -(level)+1

def calculate_level(tuple):
    if tuple[1] == 1:
        return 1, 1
    else:
        x = 3
        level = 2
        while x**2 < tuple[1]:
            level+=1
            x+=2 
        return level, ((x-2)**2)+1
        
        # Not working
        # level = int(math.sqrt(tuple[1])) - 2
        # return level, (1+2*(level-2))**2+1

def check(sT, level, count, dest):
    if sT != level and count != dest:
        return True
    return False

def proceed (sT, checkList, is_list):
    if is_list:
        print(*sT, " ")
    
    function = [up, left, down, right]
    st = [1, 0, 1, 0]
    proc = up
    
    x = 0
    while checkList[x] == 1:
        x+=1
    proc = function[x]
    sT[st[x]] = proc(sT[st[x]])
    
    return

# def steps_to_end(startNum, query, level, is_list):
#     if level == 2 and is_list:
#         print(0, 0)
#     startTuple = list(begin(level-1))
#     level-=1
#     count = startNum
#     checkList = [0,0,0,0]

#     while check(startTuple[1], level, count, query[1]):
#         count+=1
#         proceed(startTuple, checkList, is_list)
#     checkList[0] = 1
#     if count == query[1]:
#         print(*startTuple, " ")
#         return

#     while check(startTuple[0], -level, count, query[1]):
#         count+=1
#         proceed(startTuple, checkList, is_list)
#     checkList[1] = 1
#     if count == query[1]:
#         print(*startTuple, " ")
#         return

#     while check(startTuple[1], -level, count, query[1]):
#         count+=1
#         proceed(startTuple, checkList, is_list)
#     checkList[2] = 1
#     if count == query[1]:
#         print(*startTuple, " ") 
#         return

#     while check(startTuple[0], level, count, query[1]):
#         count+=1
#         proceed(startTuple, checkList, is_list)
#     checkList[3] = 1
#     if count == query[1] or (is_list and startTuple[0] == level):
#         print(*startTuple, " ") 

#     return


def steps_to_end(startNum, query, level, is_list):
    if level == 2 and is_list:
        print(0, 0)
    startTuple = list(begin(level-1))
    level-=1
    count = startNum
    while startTuple[1] != level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[1] = up(startTuple[1])
    if count == query[1]:# or (is_list and startTuple[1] == level):
        print(*startTuple, " ")
    #if count==query[1]:
        return True
    while startTuple[0] != -level and count != query[1]:                                             
        count+=1
        if is_list:                                                                                 
            print(*startTuple, " ")                                                                       
        startTuple[0] = left(startTuple[0])
    if count == query[1]:# or (is_list and startTuple[0] == -level):                                                                           
        print(*startTuple, " ")
    #if count==query[1]:
        return True
    while startTuple[1] != -level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[1] = down(startTuple[1])
    if count == query[1]:# or (is_list and startTuple[1] == -level):
        print(*startTuple, " ") 
    #if count==query[1]:
        return True
    while startTuple[0] != level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[0] = right(startTuple[0])
    if count == query[1] or (is_list and startTuple[0] == level):
        #print(count, query[1])
        print(*startTuple, " ") 
    if count == query[1]:
        return True
    #print(level, startTuple, count, query[1])
    return False

def start():
    qNum = int(input())
    queries = [[x for x in input().split()] for i in range(qNum)]

    for query in queries:
        query[1] = int(query[1])
        # print(query)
        level, start = calculate_level(query)
        # print(level, start)
        if query[0] == 'item':
            steps_to_end(start, query, level, False)
        elif query[0] == 'list':
            if query[1] == 1:
                print(0, 0)
                return
            for i in range(2,level+1):
                if i == level:             
                    steps_to_end(start, query, i, True)
                else:
                    steps_to_end(0, query, i, True)

    return 
start()
    

