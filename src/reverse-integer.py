class Solution:
    # @return an integer
    def reverse(self, x):
		if x > -10 and x < 10:
			return x
				            
		result = 0
		base = 1
		digits = []
		flag = 1
		
		if x <= -10:
			flag = -1
			x = x * flag
				      
		while x != 0:
			digits.append(x % 10)
			x = x / 10
			base = base * 10
		base = base / 10
		for i in range(0, len(digits)):
			result = result + base * digits[i]
			base = base / 10
		return result * flag