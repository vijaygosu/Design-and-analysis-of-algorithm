import time
def bubblesort(A):
    stime=time.perf_counter()
    temp=0
    for i in range(len(A)):
        for j in range(i+1):
            if A[i]<A[j]:
                A[i],A[j]=A[j],A[i]

    etime=time.perf_counter()
    timec=etime-stime
    return A,timec
def selectionsort(A):
    start_time=time.perf_counter()
    for i in range(len(A)):
        mini=i
        for j in range(i+1,len(A)):
            if A[j]<A[mini]:
                mini=j
        A[i],A[mini]=A[mini],A[i]
    end_time=time.perf_counter()
    time_taken_ms=(end_time-start_time)
    return A,time_taken_ms

A=[1,4,2,7,3,9]
Bsort,Btime=bubblesort(A)
print(Bsort,"bubble time=",Btime)
Ssort,Stime=selectionsort(A)
print(Ssort,"selection time=",Stime)
start_time = time.perf_counter()
A.sort()
end_time = time.perf_counter()
time_taken_sort = end_time - start_time
print(A, "A.sort time=", time_taken_sort)

