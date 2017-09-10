"""W is maximum space
R is the array of items
A is maximum values
T is traceback array"""
from __future__ import print_function
def knapsack_with_repetition(W,R,A,T):
	for i in range(W+1):
		val = 0
		trace = -1
		for j in range(len(R)):
			if R[j][0]<=i:
				if A[i-R[j][0]] + R[j][1]>val:
					val = A[i-R[j][0]] + R[j][1]
					trace = j
		A[i] = val
		T[i] = trace
def knapsack_topdown(W,R,A,T):
	if W==0:
		return 0,0
	elif A[W]>=0:
		return A[W],T[W]
	else:
		val = 0
		trace = -1
		for j in range(len(R)):
			if R[j][0]<=W:
				temp1,temp2 = knapsack_topdown(W-R[j][0],R,A,T)
				if temp1 + R[j][1] > val:
					val = temp1 + R[j][1]
					trace = j
		A[W] = val
		T[W] = trace
		return A[W],T[W]
W = 5
R = [[6,30],[3,14],[4,16],[2,9]]
A = [-1]*(W+1)
T = [-1]*(W+1)
print(knapsack_topdown(W,R,A,T))
#knapsack_with_repetition(W,R,A,T)
#print(A[W])
print(T)
while W>0 and T[W]>=0:
	print(R[T[W]])
	W -= R[T[W]][0]