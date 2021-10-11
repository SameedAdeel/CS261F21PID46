
def InstertionSort(Arr):
    for i in range(1,len(Arr)):
        key=Arr[i]
        j=i-1

        while j>=0 and Arr[j] > key:
            Arr[j+1]=Arr[j]
            j=j-1
        Arr[j+1]= key


def Search(Arr,s):
    list=[]
    for i in range(0,len(Arr)):
        if(s==Arr[i]):
            list.append(Arr[i])
        else:
            continue
    return list