import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#整数input
def ii(): return int(sys.stdin.readline().rstrip()) #int(input())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii()) #list(map(int,input().split()))
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
#文字列input
def ss(): return sys.stdin.readline().rstrip() #input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss()) #list(input().split())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？
#本当に貪欲法か？ DP法では？？

n=ii()
a=[]
x=[]
y=[]

for i in range(n):
    a0=ii()
    a.append(a0)
    xtemp=[]
    ytemp=[]
    for j in range(a0):
        x0,y0=mii()
        x0-=1
        xtemp.append(x0)
        ytemp.append(y0)
    x.append(xtemp)
    y.append(ytemp)

ans=0
for i in product([0,1], repeat=n):
    arr=list(deepcopy(i))


    #嘘つきは0 正直だと1 0だと反転 1だとそのまま
    temp=0
    for j in range(n):
        
        if i[j]==1:
            for k in range(a[j]):
                if i[x[j][k]]!=y[j][k]:
                    temp=1

    if temp==0:
        ans=max(ans,sum(arr))
    #ans=max(cnt,ans)
print(ans)

