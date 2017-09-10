from __future__ import print_function
def knapsack_without_repetition(W,R,A):
	for j in range(1,len(R)+1):
		for i in range(1,W+1):
			A[j][i] = A[j-1][i]
			if i>=R[j-1][0]:
				if A[j][i]<A[j-1][i-R[j-1][0]] + R[j-1][1]:
					A[j][i] = A[j-1][i-R[j-1][0]] + R[j-1][1]
def print_optimal_items(W,R,A,T,index):
	if W==0 or index==0:
		return
	if A[index][W]==A[index-1][W-R[index-1][0]] + R[index-1][1]:
		T[index-1] = 1
		print_optimal_items(W-R[index-1][0],R,A,T,index-1)
	else:
		print_optimal_items(W,R,A,T,index-1)
def knapsack_topdown(W,R,A,i):
	if i==0 or W==0:
		A[i][W] = 0
		return 0
	if A[i][W]<0:
		A[i][W] = knapsack_topdown(W,R,A,i-1)
		if W>=R[i-1][0]:
			temp = knapsack_topdown(W-R[i-1][0],R,A,i-1) + R[i-1][1]
			if A[i][W]<temp:
				A[i][W] = temp
	return A[i][W]
W = 100
R = [[6,30],[3,14],[4,16],[2,9]]
A = [[-1]*(W+1) for x in xrange(len(R)+1)]
T = [0]*(len(R))
#knapsack_without_repetition(W,R,A)
print(knapsack_topdown(W,R,A,len(R)))
for i in range(len(A)):
	for j in range(len(A[i])):
		print(A[i][j],end=" ")
	print("")
print_optimal_items(W,R,A,T,len(R))
for x in range(len(T)):
	if T[x]==1:
		print(R[x])