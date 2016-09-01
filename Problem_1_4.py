import numpy as np
import timeit
import matplotlib.pyplot as plt

def InsertionSort(A):
    for j in range(len(A)):     #dont set to array!
        key= A[j]               #insert A[j] into the sorted sequence A[0..j]
        i = j -1                # comparing to the one less       
        while i>= 0 and A[i]>key:   
            A[i+1] = A[i]           
            i= i -1
        A[i+1]=key
    return(A)


def Merge(A, front, mid, back):
    a=mid-front+1
    b=back - mid
    L=np.array(A[front:mid+1])  #new subarrays
    R=np.array(A[mid+1:back+1]) #: means choosing what parts of array
    i=0                         # not 1 like in psuedo code 
    j=0
    while front<=back and i< a and j< b:
        if L[i] <= R[j]:
            A[front] = L[i]
            i+=1            #increment
        else:
            A[front] = R[j]
            j+=1
        front+=1
    while i<a:
        A[front]=L[i]
        i+=1
        front+=1
    while j<b:
        A[front]=R[j]
        j+=1
        front+=1
    return (A)
            
def MergeSort(A, front, back):
    mid = (front + back)//2     #// mean divide and then round down
    if front+1 <back:
        MergeSort(A, front, mid)
        MergeSort(A, mid+1, back)
    Merge(A, front, mid, back)
    return (A)
     
def MergeSort2(A):
    front = 0
    back = len(A) -1
    MergeSort(A, front, back)
    return (A)


n=5

print("Insertion Sort: Worst") 
case=np.zeros(n)    
for i in range(n):
    A=np.arange(i, 0, -1)
    t=timeit.Timer(lambda: InsertionSort(A))
    case[i]= t.timeit(number=1) 
    print(t.timeit(number=1))
    plt.plot(range(n), case)
    plt.title("Worst Case")
    plt.ylabel("time")
    plt.xlabel("array size")
    plt.show()
    
print("Insertion Sort: Best")
case = np.zeros(n)
for i in range(n):
    A = np.arange(1, i+1, 1)
    t=timeit.Timer(lambda: InsertionSort(A))
    case[i] = t.timeit(number=1)
    print(t.timeit(number=1))
    plt.plot(range(n), case)
    plt.title("Best Case")
    plt.ylabel("time")
    plt.xlabel("array size")
    plt.show()

case=np.zeros(n)
print("Merge Sort:Worst")       
for i in range(n):
    A=np.arange(i, 0, -1)
    t=timeit.Timer(lambda: MergeSort2(A))
    case[i]= t.timeit(number=1)
    print(t.timeit(number=1))
    plt.plot(range(n), case)
    plt.title("Worst Case")
    plt.ylabel("time")
    plt.xlabel("array size")
    plt.show()

print("Merge Sort: Best")
case = np.zeros(n)
for i in range(n):
    A = np.arange(1, i+1, 1)
    t=timeit.Timer(lambda: MergeSort2(A))
    case[i] = t.timeit(number=1)
    print(t.timeit(number=1))
    plt.plot(range(n), case)
    plt.title("Best Case")
    plt.ylabel("time")
    plt.xlabel("array size")
    plt.show()
    
