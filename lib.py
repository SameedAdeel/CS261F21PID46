# Algorithm for the sorting purpose
# 1 InsertionSort
def InsertionSort(Arr):
    for i in range(1,len(Arr)):
        key=Arr[i]
        j=i-1

        while j>=0 and Arr[j] > key:
            Arr[j+1]=Arr[j]
            j=j-1
        Arr[j+1]= key
# 2. SelectionSort
def SelectionSort(Arr): 
    #min=0
    for i in range(len(Arr)):
        min=i

        for j in range (i+1,len(Arr)):
            if Arr[j] < Arr[min]:
                min=j

        if min!= i :
            Arr[i],Arr[min]=Arr[min],Arr[i]
# Merge Function
def Merge(A,low,m,high):
    L=[]
    R=[]
    o=m+1
    for i in range(low,m+1):
        L.append(A[i])
        
    for j in range(o,high+1):
        R.append(A[j])
        
    i=0
    j=0
    x=[]
    while i< len(L) and j < len(R):
        if(L[i]<R[j]):
            x.append(L[i])
          
            i=i+1
        else:
            x.append(R[j])
            j=j+1
    if i!= len(L):
        while i<len(L):
            x.append(L[i])
            i=i+1
    if j!= len(R):
        while j<len(R):
            x.append(R[j])
            j=j+1
    k=low
    for each in x:
        A[k]=each 
        k=k+1

# 3. MergeSort
def MergeSort(arr,l,h):
    if l < h:
        m=int((l+h-1)/2)
        MergeSort(arr,l,m)
        MergeSort(arr,m+1,h)
        Merge(arr,l,m,h)

def Search(Arr,s):
    list=[]
    for i in range(0,len(Arr)):
        if(s==Arr[i]):
            list.append(Arr[i])
        else:
            continue
    return list

from math import floor
def Bucket(arr,n):
    bucket=[[] for f in range (n)]
    output=[]
    for i in range (0,n-1):
        bucket[(floor(n*arr[i]))].append(arr[i])
    
    for i in range (0,len(bucket)):
        InsertionSort(bucket[i])
    for each in bucket:
        output += each
    return output

def ConuntingSort(arr):
    k= max(arr)-min(arr)
    size=len(arr)
    count=[0]*(k+1)
    output=[0]*size
    index=-1
    P=[]
    N=[]
    for i in range (size):
        j=arr[i]
        count[j]+=1
    
    for i in range (1,k+1):
        count[i]+=count[i-1]
    
    for i in range (size-1,-1,-1):
        j = arr[i]
        count[j]-=1
        output[count[j]]=arr[i]
    for i in range (0,size):
        if output[i] >= 0 :
            P.append(output[i])
        else:
            N.append(output[i])
    print(P)
    print(N)
    return N+P

def partition(arr,low,high):
    
    pivot=arr[high]
    
    i=low-1
    
    for j in range (low,high):
        
        if arr[j] < pivot :
            i = i+1
            arr[i],arr[j]=arr[j],arr[i]
    
    
    arr[i+1],arr[high]=arr[high],arr[i+1]
    
    return i+1

def QuickSelect(arr,left,right,k):
    if left == right:
        return arr[left]
    print(right)
    pivotIndex = partition(arr,left,right)
    if k == pivotIndex :
        return arr[k-1]
    elif k < pivotIndex :
        right = pivotIndex -1
        return(quickSelect(arr,left,pivotIndex-1,k))
    
    else :
        left = pivotIndex+1
        return(quickSelect(arr,pivotIndex+1,right,k))


def QuickSort(arr,low,high):
    if low < high :
        pi= partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)


   
