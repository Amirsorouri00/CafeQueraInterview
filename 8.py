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
def merge(arr, l, m, r): 
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

	while i < n1 and j < n2 : 
		if L[i] >= R[j]: 
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
def merge_sort(arr,l,r): 
	if l < r: 

		# Same as (l+r)//2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))//2

		# Sort first and second halves 
		merge_sort(arr, l, m) 
		merge_sort(arr, m+1, r) 
		merge(arr, l, m, r) 

static = 2
number = [0]

def can(chocolets):
    arr = chocolets[:]
    size = len(arr)
    temp = []
    while size > 1:
        merge_sort(arr, 0, size-1)
        # print(arr, temp, size)
        temp = []
        for i in range(0, int(size/2)):
            x = (arr[i] - arr[size-i-1])
            temp.append(x)
        if size%2 != 0:
            temp.append(arr[int(size/2)])
        size = len(temp)
        arr = temp
    if arr[0] == 0:
        return True
    else:
        return False
# last_time = [0]
def rearrenge(chocolets, size):
    start, end = [0,size-1]
    ischanged = False
    this_time = 0
    while start < end:
        if chocolets[start] > chocolets[end]:
            ischanged = True
            chocolets[start]-=1
            chocolets[end]+=1
            number[0]+=static
        start+=1
        end-=1

    return ischanged
def arrange(chocolets, size):
    start, end = [0,size-1]
    ischanged = True
    while ischanged == True:
        ischanged = False
        merge_sort(chocolets, 0, size-1)
        # print(chocolets)
        ischanged = rearrenge(chocolets, size)

    return

def start():
    size = int(input())

    chocolets = invr()
    if len(chocolets) != size:
        print("Wrong inputs")
    else:
        if can(chocolets) == False:
            print("-1")
        else:
            arrange(chocolets, size)
            print(number[0])
    return

start()