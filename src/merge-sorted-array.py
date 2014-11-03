class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		if A == None or B == None:
			return
		if m < 0 or n <= 0:
			return
		pB = n - 1
		pM = m + n - 1
		if m > 0:
			pA = m - 1
		
			while pA >= 0 and pB >= 0:
				if A[pA] >= B[pB]:
					A[pM] = A[pA]
					pA = pA - 1
				else:
					A[pM] = B[pB]
					pB = pB - 1
				pM = pM - 1
			# print pA
			# print pB
			# print pM
			for i in range(0, pA + 1):
				A[pM] = A[pA]
				pM = pM - 1
				pA = pA - 1
		for i in range(0, pB + 1):
			A[pM] = B[pB]
			pM = pM - 1
			pB = pB - 1