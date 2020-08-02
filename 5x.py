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

def calculate_level(tuple, level, count):
    count = 1
    if tuple[1] == 1:
        return 1
    sum = 0
    while count < tuple[1]:
        constant = level * 2
        sum = (1 + constant)*4 - 4
        count+= sum
        level+=1
    return level, count-sum+1

def steps_to_end(startNum, query, level, is_list):
    #if level == 0:
    #    print(0, 0)
    #    return
    startTuple = list(begin(level-1))
    level-=1
    count = startNum
    while startTuple[1] <= level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[1] = up(startTuple[1])
    if count == query[1]:
        print(*startTuple, " ")
        return True
    while startTuple[0] >= -level and count != query[1]:                                             
        count+=1
        if is_list:                                                                                 
            print(*startTuple, " ")                                                                       
        startTuple[0] = left(startTuple[0])
    if count == query[1]:                                                                           
        print(*startTuple, " ")
        return True
    while startTuple[1] >= -level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[1] = down(startTuple[1])
    if count == query[1]:
        print(*startTuple, " ") 
        return True
    while startTuple[0] <= level and count != query[1]:
        count+=1
        if is_list:
            print(*startTuple, " ")
        startTuple[0] = right(startTuple[0])
    if count == query[1]:
        #print(count, query[1])
        print(*startTuple, " ") 
        return True
#    print(level, startTuplecount, query[1])
    return False

def start():
    qNum = int(input())
    queries = [[x for x in input().split()] for i in range(qNum)]

    for query in queries:
        query[1] = int(query[1])
        #print(query)
        level, start = calculate_level(query, 1, 1)
        #print(level, start)
        if query[0] == 'item':
            x=0
            steps_to_end(start, query, level, False)
        elif query[0] == 'list':
            x=0
            for i in range(0,level+1):
                if i == level:                
                    steps_to_end(start, query, i, True)
                else:
                    level, start = calculate_level(query, 1, 1)
                    steps_to_end(0, query, i, True)
        else:
            print("wrong input.")
            return 
    return 
start()
    

