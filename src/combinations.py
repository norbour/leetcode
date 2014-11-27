class Solution:
	# @return a list of lists of integers
	def combine(self, n, k):
		result = []
		if n <= 0 or k <= 0 or n < k:
			return reuslt
		for i in range(1, n - k + 2):
			combination = []
			combination.append(i)
			self.combineCore(i + 1, n, k - 1, combination, result)
		return result

	def combineCore(self, begin, n, k, combination, result):
		if k == 0:
			result.append(copy.copy(combination))
			return
		if begin == n + 1:
			return
		combination.append(begin)
		self.combineCore(begin + 1, n, k - 1, combination, result)
		combination.pop()
		self.combineCore(begin + 1, n, k, combination, result)