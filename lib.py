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
        m=int((l+r-1)/2)
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



   
