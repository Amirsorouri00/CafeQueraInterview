def rotation(matrix, r): 
    for z in range(r):
        top = 0
        bottom = len(matrix)-1

        left = 0
        right = len(matrix[0])-1

        while left < right and top < bottom:
            prev = matrix[top+1][right]
            for i in range(right,left-1,-1):
                curr = matrix[top][i]
                matrix[top][i]= prev
                prev =curr
            top += 1
            for i in range(top,bottom+1):
                curr = matrix[i][left]
                matrix[i][left]=prev
                prev=curr
            left += 1
            for i in range(left,right+1):
                curr =matrix[bottom][i]
                matrix[bottom][i]=prev
                prev = curr
            bottom -=1
            for i in range(bottom,top-1,-1):
                curr = matrix[i][right]
                matrix[i][right]=prev
                prev = curr
            right -=1


def displayMatrix(M, N, matrix):
    # global M, N, matrix
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

def start():
    m,n,k = input().split()
    matrix = [[x for x in input().split()] for i in range(int(m))]
    rotation(matrix, int(k))
    displayMatrix(int(m), int(n), matrix)


start()