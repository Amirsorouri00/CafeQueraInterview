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
def merge(arr, l, m, r, decrease): 
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
            if L[i] >= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
        else:
            if L[i] <= R[j]: 
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
def merge_sort(arr,l,r, decrease): 
	if l < r: 

		# Same as (l+r)//2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))//2

		# Sort first and second halves 
		merge_sort(arr, l, m, decrease) 
		merge_sort(arr, m+1, r, decrease) 
		merge(arr, l, m, r, decrease) 

def calc(mintowers, maxtowers, size, m, d):
    if m == size:
        mintowers[size-1]+=d
    else:
        tmp = []
        tmp2 = [0 for i in range(0, size)]

        for i in range(0, size):
            tmp.append(mintowers[size-1]-mintowers[i])

        x = m*d
        k = size-1
        tmpsize = size - 1

        for g in range(0, d):
            i = 0
            index = 0
            while i < m:
                if x == 0:
                    break
                if tmpsize > 0 and tmp[index] == 0:
                    tmpsize-=1
                    index+=1
                    continue
                elif tmpsize == 0:
                    tmp2[k]+=1
                    if k == 0:
                        k = size-1
                    else:
                        k-=1
                    x-=1
                    i+=1
                else:
                    i+=1
                    tmp[index]-=1
                    index+=1
                    x-=1

        for i in range(0, size):
            mintowers[i] += (tmp2[i] - tmp[i])

    maxtowers[0]+=d

def start():
    n, m, d = invr()
    towers = invr()
    mintowers = towers[:]
    maxtowers = towers[:]
    merge_sort(maxtowers, 0, n-1, True)
    # print(towers)
    merge_sort(mintowers, 0, n-1, False)
    # print(towers)
    calc(mintowers, maxtowers, n, m, d)
    # merge_sort(mintowers, 0, n-1, False)
    print(maxtowers[0], mintowers[n-1])

start()