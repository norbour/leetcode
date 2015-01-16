class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if num == None:
            raise ValueError("Invlaid array input!")
        length = len(num)
        if length == 0:
            raise ValueError("Invlaid array input!")
        majority = num[0]
        time = 1
        for i in range(1, length):
            if time == 0:
                majority = num[i]
                time = 1
            elif majority == num[i]:
                time = time + 1
            else:
                time = time - 1
        return majority