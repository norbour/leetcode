class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		if A == None:
			return
		length = len(A)
		if length == 0:
			return
		max = -1000
		count = 0
		for i in range(0, length):
			if count <= 0:
				count = A[i]
			else:
				count = count + A[i]
			if count > max:
				max = count
			i = i + 1
		return max
        