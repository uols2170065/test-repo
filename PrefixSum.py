송예범, 202302019, 컴퓨터공학과

import time, random

def prefixSum1(X, n):
	S = [0] * n
	for i in range(n):
		for j in range(i+1):
			S[i]+=X[j]
			
	# code for prefixSum1
	
def prefixSum2(X, n):
	S=[0]*n
	S[0] = X[0]
	for i in range(1, n):
		S[i] = S[i-1] + X[i]
	# code for prefixSum2
	
random.seed()		# random 함수 초기화

n = int(input())
# n 입력받음

X = [random.randint(-999,999) for _ in range(n)]
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움

before1 = time.process_time()
prefixSum1(X,n)
after1 = time.process_time()
# prefixSum1 호출

before2 = time.process_time()
prefixSum2(X,n)
after2 = time.process_time()
# prefixSum2 호출

print(after1 - before1)
print(after2 - before2)

# 두 함수의 수행시간 출력

