from __future__ import print_function


def edit_distance(s1,s2,D):
	n = len(s1)
	m = len(s2)
	for i in range(m+1):
		D[0][i] = i
	for i in range(n+1):
		D[i][0] = i
	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1]==s2[j-1]:
				min_distance = D[i-1][j-1]
			else:
				min_distance = D[i-1][j-1] + 1
			if min_distance>D[i-1][j] + 1:
				min_distance = D[i-1][j] + 1
			if min_distance>D[i][j-1] + 1:
				min_distance = D[i][j-1] + 1
			D[i][j] = min_distance
	print(D[n][m])
	s1list = list(s1)
	s2list = list(s2)
	while n>0 or m>0:
		if n>0 and D[n][m] == D[n-1][m] + 1:
			s2list.insert(n-1,"-")
			n-=1
		elif m>0 and D[n][m] == D[n][m-1] + 1:
			s1list.insert(m,"-")
			m-=1
		else:
			n-=1
			m-=1
	for x in s1list:
		print(x,end="")
	print("")
	for x in s2list:
		print(x,end="")
	print("")
s1 = raw_input()
s2 = raw_input()
D = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]
edit_distance(s1,s2,D)