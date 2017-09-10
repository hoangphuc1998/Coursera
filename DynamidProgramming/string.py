from __future__ import print_function
s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
n = len(s1)
m = len(s2)
o = len(s3)
R = [[[0] * (o+1) for x in xrange(m+1)] for y in xrange(n+1)]
def longest_substring():
	for i in range(1,n+1):
		for j in range(1,m+1):
			for k in range(1,o+1):
				if s1[i-1]==s2[j-1] and s2[j-1]==s3[k-1]:
					R[i][j][k] = R[i-1][j-1][k-1] + 1
				else:
					R[i][j][k] = R[i-1][j-1][k-1]
				val = R[i][j][k]
				if val<R[i-1][j][k]:
					val = R[i-1][j][k]
				if val<R[i][j-1][k]:
					val = R[i][j-1][k]
				if val<R[i][j][k-1]:
					val = R[i][j][k-1]
				R[i][j][k] = val
def print_string(i,j,k):
	if i==0 or j==0 or k==0:
		return
	if R[i][j][k] == R[i-1][j][k]:
		print_string(i-1,j,k)
	elif R[i][j][k] == R[i][j-1][k]:
		print_string(i,j-1,k)
	elif R[i][j][k] == R[i][j][k-1]:
		print_string(i,j,k-1)
	elif R[i][j][k] == R[i-1][j-1][k-1]:
		print_string(i-1,j-1,k-1)
	else:
		print_string(i-1,j-1,k-1)
		print(s1[i-1],end=" ")
longest_substring()
print(R[n][m][o])
print_string(n,m,o)
print("")