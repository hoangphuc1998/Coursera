def gold(A,w,R,i):
	if w==0 or i==0:
		R[i][w] = 0
		return 0
	if R[i][w]<0:
		R[i][w] = gold(A,w,R,i-1)
		if w>=A[i-1]:
			if R[i][w]<gold(A,w-A[i-1],R,i-1) + A[i-1]:
				R[i][w] = R[i-1][w-A[i-1]] + A[i-1]
	return R[i][w]
def reconstruct_optimal_solution(A,w,R,i):
	if w==0 or i==0:
		return
	if w>=A[i-1]:
		if R[i-1][w-A[i-1]] + A[i-1] == R[i][w]:
			reconstruct_optimal_solution(A,w-A[i-1],R,i-1)
			print(A[i-1])
			return
	reconstruct_optimal_solution(A,w,R,i-1)
w = input()
A = [int(x) for x in raw_input().split(" ")]
R = [[-1]*(w+1) for x in xrange(len(A)+1)]
print(gold(A,w,R,len(A)))
reconstruct_optimal_solution(A,w,R,len(A))