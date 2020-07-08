size1 = [5, 6]
mat11 = [1, 2, 10, 34, 54]
mat12 = [9, 82, 23, 54, 1, 10]
output11 = 3
output12 = [1, 10, 54]

size2 = [3, 4]
mat21 = [10, 20, 30]
mat22 = [5, 15, 25, 35]
output21 = 0
output22 = []

sizes = [size1, size2]
mat1s = [mat11, mat21]
mat2s = [mat12, mat22]
output1s = [output11, output21]
output2s = [output12, output22]


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
def mergeSort(arr,l,r): 
	if l < r: 

		# Same as (l+r)//2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))//2

		# Sort first and second halves 
		mergeSort(arr, l, m) 
		mergeSort(arr, m+1, r) 
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


def intersection(lst1, lst2): 
    output_mat = list(set(lst1) & set(lst2))

    return len(output_mat), output_mat


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
    mergeSort(mat1, 0, size[0] - 1)
    mergeSort(mat2, 0, size[1] - 1)
    
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

def test():
    for i in range(0, 2):
        size = sizes.pop(0)
        mat1 = mat1s.pop(0)
        mat2 = mat2s.pop(0)
        out1 = output1s.pop(0)
        out2 = output2s.pop(0)

        o1, o2 = findShare(size, mat1, mat2)
        if o1 == out1:
            print(o1)
            if o1 != 0:
                o2.sort()
                out2.sort()
                if o2 == out2:
                    print(o2)
                else:
                    print("something went wrong in: ", size, mat1, mat2, out1, out2, o1, o2)
        else:
            print("2:something went wrong in: ", size, mat1, mat2, out1, out2, o1, o2)

test()


# Driver code to test above 
# arr = [12, 11, 13, 5, 6, 7] 
# n = len(arr) 
# print ("Given array is") 
# for i in range(n): 
# 	print ("%d" %arr[i]), 

# mergeSort(arr,0,n-1) 


# This code is contributed by Mohit Kumra 
