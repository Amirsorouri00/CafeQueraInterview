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



# mat1 = [int(x) for x in sys.stdin.readline().split()]
mat1 = invr()

print(list(mat1), "\n", len(list(mat1)))