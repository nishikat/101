from scipy import linalg
import numpy as np
##############################################
#Problem 1
#A= np.array([[1,2],[3,5], [1,1]])
#x= np.array([1,5])

def matmult(A,x):
    rows = len(A)
    b = [0]*rows
    #irange = range(len(x))
    sum = 0
    j=0
    i=0
    #for j in range(rows):
    while (j<rows):
        r = A[j]
        #for i in irange:
        while (i<len(x)):
            sum+= r[i]*x[i]
            b[j]=sum            
            i+=1
        i=0
        sum=0
        j+=1
    return b

#print(matmult(A,x))

################################################
# Problem 2
def hadmat(k):
    a = np.array([[1]])
    b= -a
    if k==0:
        return a
    for i in range(0, k):
            x= np.concatenate((a, a), axis=1)
            y= np.concatenate((a,b), axis=1)
            z= np.concatenate((x,y), axis=0)
            a=z
            b=-a
    return a
    
#print(hadmat(3))
    
##################################################
# Problem 4
def hadmatmult(H, x):
    mid=(len(x))//2
    top=np.array(x[:mid])
    bot=np.array(x[mid:])
    if len(top)>1 and len(bot)>1:
        m=hadmatmult(H[:mid][:mid], top)
        n=hadmatmult(H[:mid][:mid], bot)
    else:
        m= top
        n= bot
    add= m+n
    sub= m-n
    b=np.concatenate((add,sub), axis=0)
    return b
    
H= linalg.hadamard(1)   
x= np.array([1,2,3,4])   
print(hadmatmult(H,x))

###################################################
#Problem 5

    