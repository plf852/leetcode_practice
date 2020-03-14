a = [2,1]
def partition(data,start,end):
    pivot = data[start]
    while start<end:
        while start<end and data[end]>=pivot:
            end -= 1
        while start<end and data[start]<pivot:
            start += 1
        data[start],data[end]=data[end],data[start]
    return start
def quickSort(data,start,end):
    if start<end:
        pi = partition(data,start,end)
        quickSort(data,start,pi-1)
        quickSort(data,pi+1,end)

print('origin:',a)
quickSort(a,0,len(a)-1)
print('after:',a)