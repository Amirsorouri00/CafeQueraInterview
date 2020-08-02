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

# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
# True ==> Descending
# False ==> Ascending
def merge(arr, l, m, r, decrease, y): 
    n1 = m - l + 1
    n2 = r- m 

    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 

    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 

    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 

    # Merge the temp arrays back into arr[l..r] 
    i = 0	 # Initial index of first subarray 
    j = 0	 # Initial index of second subarray 
    k = l	 # Initial index of merged subarray 

    while i < n1 and j < n2: 
        if decrease == True:
            if y == True:
                if L[i][1] >= R[j][1]: 
                    arr[k] = L[i] 
                    i += 1
                else: 
                    arr[k] = R[j] 
                    j += 1
            else:
                if L[i][0] >= R[j][0]: 
                    arr[k] = L[i] 
                    i += 1
                else: 
                    arr[k] = R[j] 
                    j += 1
            k += 1
        else:
            if y == True:
                if L[i][0] <= R[j][0]: 
                    arr[k] = L[i] 
                    i += 1
                else: 
                    arr[k] = R[j] 
                    j += 1
            else:
                if L[i][0] <= R[j][0]: 
                    arr[k] = L[i] 
                    i += 1
                else: 
                    arr[k] = R[j] 
                    j += 1
            k += 1

	# Copy the remaining elements of L[], if there 
	# are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def merge_sort(arr,l,r, decrease, y): 
	if l < r: 

		# Same as (l+r)//2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))//2

		# Sort first and second halves 
		merge_sort(arr, l, m, decrease) 
		merge_sort(arr, m+1, r, decrease) 
		merge(arr, l, m, r, decrease) 


# Binary Search finds in Descending list
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid][0] == val:
            index = mid
        else:
            if val<lys[mid][0]:
                last = mid -1
            else:
                first = mid +1
    return index

def issquare(arr, y, minx, maxx):
    # size = len(arr)
    if minx == maxx and arr[minx][1] == y:
        return 1
    elif minx == maxx and arr[minx][1] != y:
        return -1
    else:
        size = maxx + minx #len(arr)
        mid = size//2
        res = issquare(arr, y, minx, mid)
        if res != 1:
            return res
        res = issquare(arr, y, minx, mid)
        return res

def exist(arr, n, m, k):
    minx = arr[0][0]
    maxx = arr[k-1][0]
    maxtmp = minx + (m - 1)
    arry = arr[:]
    merge_sort(arry, 0, k-1, True, True)
    miny = arry[0][1]
    maxy = arry[k-1][1]
    while maxtmp <= maxx:
        minxindex = BinarySearch(arr, minx)
        if minxindex == -1
            minx+=1
            maxtmp+=1
            continue
        maxtmpindex = BinarySearch(arr, maxtmp)
        if maxtmpindex == -1
            minx+=1
            maxtmp+=1
            continue
        
        while arr[minindex][0] == minx and arr[maxtmpindex][1] == maxtmp:
            
            if arr[maxtmp][1] != arr[maxx][1]:
                minx+=1
                maxtmp+=1
                continue
            else:
                nohope = True
                y = arr[maxtmp][1]
                if maxy - y < m - 1:# and y - miny < m-1:
                    minx+=1
                    maxtmp+=1
                    continue

                else:

                issquare(arr, arr[maxtmp])

def start():
    n, m = invr()
    k = int(input())
    arr = []
    for i in range(0, k):
        arr.append(invr()) 
    merge_sort(arr, 0, k-1, False, False)
    
    print(arr)
    print(BinarySearch(arr, 1))

start()