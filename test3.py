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



def start():
    inp = int(input())

    states = (2**inp)//2
    statesNo = states//2
    s=''
    startStates = [s+'v' for i in range(0, inp)]
    listStates = []
    listStates.append(startStates)
    for i in range(1, (inp//2)+1):
        tmp = listStates[i-1][:]
        tmp[i] = 'h'
        listStates.append(tmp)

    finalRes = [0 for i in range(0, inp//2+1)]
    # print(listStates, inp//2)
    for i in range(0, inp//2+1):
        horizAreas = 0
        vertAreas = 0

        firstVer = True
        firstHor = True
        # print(listStates[i])
        for  c in listStates[i]:
            if c == "v" and firstVer == True and firstHor == False:
                finalRes[i]=horizAreas*2
                vertAreas+=2
                firstVer = False
            elif c == 'v' and firstVer == True and firstHor == True:
                finalRes[i]+=2
                vertAreas+=2
                firstVer = False
            elif c == 'v' and firstVer == False and firstHor == True:
                finalRes[i]+=1
                vertAreas+=1
            elif c == 'v' and firstVer == False and firstHor == False:
                finalRes[i]+=horizAreas
                vertAreas+=1
            if c == "h" and firstHor == True and firstVer == False:
                finalRes[i]=vertAreas*2
                horizAreas+=2
                firstHor = False
            elif c == 'h' and firstHor == True and firstVer == True:
                finalRes[i]+=2
                horizAreas+=2
                firstHor = False
            elif c == 'h' and firstHor == False and firstVer == True:
                finalRes[i]+=1
                horizAreas+=1
            elif c == 'h' and firstHor == False and firstVer == False:
                finalRes[i]+=vertAreas
                horizAreas+=1
            # print(finalRes[i])
    
    # print(statesNo, finalRes)
    merge_sort(finalRes, 0, (inp//2), True)
    
    print(finalRes[0])


start()