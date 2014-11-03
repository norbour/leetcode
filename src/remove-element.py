class Solution:
	# @param    A       a list of integers
	# @param    elem    an integer, value need to be removed
	# @return an integer
	def removeElement(self, A, elem):
		if A == None:
			return 0
		length = len(A)
		if length == 0:
			return 0
		head = 0
		tail = length - 1
		count = 0
		while head <= tail:
			while tail >= 0 and A[tail] == elem:
				tail = tail - 1
				count = count + 1
			while head <= length - 1 and A[head] != elem:
				head = head + 1
			if head < tail:
				temp = A[tail]
				A[tail] = A[head]
				A[head] = temp
				head = head + 1
				tail = tail - 1
				count = count + 1

		for i in range(0, count):
			A.pop()

		return length - count