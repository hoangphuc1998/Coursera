def change_money(M,n,A,T):
	for i in range(1,n+1):
		min_change = n + 1
		money_type = 0
		for x in M:
			if x==i:
				min_change = 1
				money_type = 0
				break
			elif i-x>0:
				if A[i-x]+1<min_change:
					min_change = A[i-x]+1
					money_type = x
		A[i] = min_change
		T[i] = money_type
	if A[n] == n+1:
		print("Not able to change")
	else:
		i = n
		while T[i]!=0:
			print(T[i])
			i = i - T[i]
		print(i)
n = 40
M = [8,20,30,2]
A = [0]*(n+1)
T = [0]*(n+1)
change_money(M,n,A,T)