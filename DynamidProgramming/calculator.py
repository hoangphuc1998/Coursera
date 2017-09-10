from __future__ import print_function
def calculator(n,A):
	for i in range(2,n+1):
		val = A[i-1] + 1
		if i%2==0 and val>A[i/2]+1:
			val = A[i/2] + 1
		if i%3==0 and val > A[i/3] + 1:
			val = A[i/3] + 1
		A[i] = val
def print_optimal_solution(n,A):
	if n==1:
		print(n,end=" ")
		return
	if n%2==0 and A[n]==A[n/2]+1:
			print_optimal_solution(n/2,A)
	elif n%3==0 and A[n] == A[n/3]+1:
			print_optimal_solution(n/3,A)
	else:
		print_optimal_solution(n-1,A)
	print(n,end=" ")

n = 96234
A = [0] * (n+1)
calculator(n,A)
print(A[n])
print_optimal_solution(n,A)
print("")