from collections import deque

def max_subarray(lst, k):
	q = deque()
	for i in range(k):
		while q and lst[i] >= lst[q[-1]]:
			q.pop()
		q.append(i)

	for i in range(k, len(lst)):
		print(lst[q[0]])	
		while q and q[0] <= i - k:
			q.popleft()
		while q and lst[i] >= lst[q[-1]]:
			q.pop()
		q.append(i)
	print(lst[q[0]])

# Tests:
lst = [10, 5, 2, 7, 8, 7]
k = 3
# Given: returns [10, 7, 8, 8]
print(max_subarray(lst, k))

# k = 1: returns original list
k = 1
print(max_subarray(lst, k))



