import sys
input = sys.stdin.readline
# Python program for implementation of MergeSort 

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
def merge_sort(arr,l,r): 
	if l < r: 

		# Same as (l+r)//2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))//2

		# Sort first and second halves 
		merge_sort(arr, l, m) 
		merge_sort(arr, m+1, r) 
		merge(arr, l, m, r) 


# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 



# Iterative Merge sort (Bottom Up) 

# Iterative mergesort function to 
# sort arr[0...n-1] 
def mergeSort(a): 
	
	current_size = 1
	
	# Outer loop for traversing Each 
	# sub array of current_size 
	while current_size < len(a) - 1: 
		
		left = 0
		# Inner loop for merge call 
		# in a sub array 
		# Each complete Iteration sorts 
		# the iterating sub array 
		while left < len(a)-1: 
			
			# mid index = left index of 
			# sub array + current sub 
			# array size - 1 
			mid = min((left + current_size - 1),(len(a)-1)) 
			
			# (False result,True result) 
			# [Condition] Can use current_size 
			# if 2 * current_size < len(a)-1 
			# else len(a)-1 
			right = ((2 * current_size + left - 1, 
					len(a) - 1)[2 * current_size 
						+ left - 1 > len(a)-1]) 
							
			# Merge call for each sub array 
			merge(a, left, mid, right) 
			left = left + current_size*2
			
		# Increasing sub array size by 
		# multiple of 2 
		current_size = 2 * current_size 

# Merge Function 
def merge(a, l, m, r): 
	n1 = m - l + 1
	n2 = r - m 
	L = [0] * n1 
	R = [0] * n2 
	for i in range(0, n1): 
		L[i] = a[l + i] 
	for i in range(0, n2): 
		R[i] = a[m + i + 1] 

	i, j, k = 0, 0, l 
	while i < n1 and j < n2: 
		if L[i] > R[j]: 
			a[k] = R[j] 
			j += 1
		else: 
			a[k] = L[i] 
			i += 1
		k += 1

	while i < n1: 
		a[k] = L[i] 
		i += 1
		k += 1

	while j < n2: 
		a[k] = R[j] 
		j += 1
		k += 1

# Contributed by Madhur Chhangani [RCOEM] 

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def findShare(size, mat1, mat2):
    merge_sort(mat1, 0, size[0] - 1)
    merge_sort(mat2, 0, size[1] - 1)
    
    # mergeSort(mat1) 
    # mergeSort(mat2) 

    # quickSort(mat1, 0, size[0] - 1) 
    # quickSort(mat2, 0, size[1] - 1)

    # print(mat1, mat2)

    min_index = size.index(min(size))
    mat_src = []
    mat_dest = []
    if min_index == 0:
        mat_src = mat1
        mat_dest = mat2
    else:
        mat_src = mat2
        mat_dest = mat11
    
    output_size = 0
    output_mat = []
    for i in mat_src:
        o = BinarySearch(mat_dest, i)
        if o == -1:
            continue
        else:
            output_size+=1
            output_mat.append(mat_dest[o])
    return output_size, output_mat

def intersection(lst1, lst2): 
    output_mat = list(set(lst1) & set(lst2))

    return len(output_mat), output_mat


def start():
    i = 0
    # size = [int(x) for x in input("Enter a two value: ").split()]
    # mat1 = [int(x) for x in input("Enter " + str(size[0]) + "value: ").split()]
    # mat2 = [int(x) for x in input("Enter " + str(size[1]) + " value: ").split()]

    size = [int(x) for x in input().split()]
    mat1 = [int(x) for x in input().split(maxsplit=999999)[:999999]]
    mat2 = [int(x) for x in input().split(maxsplit=999999999)[:999999999]]

    
    o1, o2 = findShare(size, mat1, mat2)
    # o1, o2 = intersection(mat1, mat2)

    print(o1)
    if o1 != 0:
        print(*o2, sep = " ")
    
start()