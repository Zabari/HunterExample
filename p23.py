import itertools as it
from operator import mul
import functools as func
import math as m
import time
timey=time.time()
d={}
def findPrime(n):
    i=2
    ret=[]
    oN=n
    while ((n!=1)):
        if ((n%i)==0):
            ret.append(i)
            n=n/i
        else:
            i+=1
            if ((i>m.sqrt(oN)) and (oN==n)):
                ret.append(oN)
                break
    return ret
def propFactSum(L):
    tmpL=[]
    tmpSet=set()
    num=0
    ret=0
    for num in range(len(L)-1):
        for combo in it.combinations(L,num+1):
            tmpSet.add(combo)
    tmpL=list(tmpSet)
    for i in range(len(tmpL)):
         tmpL[i]=list(tmpL[i])
         tmpL[i]=func.reduce(mul,tmpL[i] , 1)
         ret+=tmpL[i]

    return ret+1

num=2
#14062
#it.combinations_with_replacement()
L=[]
#print(propFactSum(findPrime(28123)))
while (num<=28123):
    x=findPrime(num)
    if len(x)>1:
        x=propFactSum(x)
        if (x>num):
            L.append(num)
    num+=1
#print(L)
L2=set()
for combo in it.combinations_with_replacement(L,2):
    if ((combo[0]+combo[1])<=28123):
        L2.add(combo[0]+combo[1])
# print(sum(L2))
final=(28123)*(28124)/2

final=final-sum(L2)
print(final)
print(time.time()-timey)
