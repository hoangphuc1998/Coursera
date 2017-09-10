from __future__ import print_function
#read input
string = raw_input()
"""
Constraints:
1: multiply
2: plus
3: subtract
"""
n = len(string)
temp = 0
A = []
op = []
for i in range(n):
	if string[i].isdigit():
		temp = temp*10 + int(string[i])
	else:
		A.append(temp)
		temp = 0
		if string[i]=="*":
			op.append(1)
		elif string[i]=="+":
			op.append(2)
		else:
			op.append(3)
A.append(temp)
n = len(A)
#m is the smallest value and M is the largest value
m = [[0]*n for x in xrange(n)]
M = [[0]*n for x in xrange(n)]
def find_min_max(L):
	min_val = L[0]
	max_val = L[1]
	for x in range(2,len(L)):
		if L[x]>max_val:
			max_val=L[x]
		if L[x]<min_val:
			min_val = L[x]
	return min_val,max_val
def min_and_max(i,j):
	min_val = 9999999999
	max_val = -9999999999
	for k in range(i,j):
		if op[k]==1:
			a = M[i][k] * M[k+1][j]
			b = M[i][k] * m[k+1][j]
			c = m[i][k] * m[k+1][j]
			d = m[i][k] * M[k+1][j]
		elif op[k]==2:
			a = M[i][k] + M[k+1][j]
			b = M[i][k] + m[k+1][j]
			c = m[i][k] + m[k+1][j]
			d = m[i][k] + M[k+1][j]
		else:
			a = M[i][k] - M[k+1][j]
			b = M[i][k] - m[k+1][j]
			c = m[i][k] - m[k+1][j]
			d = m[i][k] - M[k+1][j]
		min_val,max_val = find_min_max([min_val,max_val,a,b,c,d])
	return min_val,max_val

R = []
def placing_parenthesis():
	n = len(A)
	for i in range(n):
		m[i][i] = A[i]
		M[i][i] = A[i]
	for s in range(1,n):
		for i in range(n-s):
			j = i + s
			m[i][j],M[i][j] = min_and_max(i,j)
	return M[0][n-1]
def find_max(L):
	max_val = L[0]
	for i in range(1,len(L)):
		if L[i]>max_val:
			max_val=L[i]
	return max_val
def reconstruct_optimal_solution(i,j):
	if i==j:
		return
	for k in range(i,j+1):
		if op[k]==1:
			a = M[i][k] * M[k+1][j]
			b = M[i][k] * m[k+1][j]
			c = m[i][k] * m[k+1][j]
			d = m[i][k] * M[k+1][j]
		elif op[k]==2:
			a = M[i][k] + M[k+1][j]
			b = M[i][k] + m[k+1][j]
			c = m[i][k] + m[k+1][j]
			d = m[i][k] + M[k+1][j]
		else:
			a = M[i][k] - M[k+1][j]
			b = M[i][k] - m[k+1][j]
			c = m[i][k] - m[k+1][j]
			d = m[i][k] - M[k+1][j]
		if M[i][j] == find_max([a,b,c,d]):
			R.append([i,k])
			R.append([k+1,j])
			reconstruct_optimal_solution(i,k)
			reconstruct_optimal_solution(k+1,j)
			break
print(placing_parenthesis())
for i in range(n):
	for j in range(n):
		print(M[i][j],end=" ")
	print("")
reconstruct_optimal_solution(0,len(A)-1)
print(R)