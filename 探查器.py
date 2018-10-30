def swap(lyst,i,j,profiler):
    profiler.exchagne()             #自增交换
    tmp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=tmp

def selectionsort(lyst,profiler):
    i=0
    while i<len(lyst)-1:
        minIndex=i
        j=i+1
        while j<len[lyst]:
            profiler.comparsion()       #自增比较
            if lyst[j]<lyst[minIndex]:
                j=minIndex
            j+=1
    if minIndex!=i:
        swap(lyst,minIndex,i)
        i+=1
