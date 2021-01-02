class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_size = pow(2, len(nums))
        r = []
        for i in range(list_size):
            binary = ('{0:0%db}' % len(nums)).format(i)
            tmp = []
            for j in range(len(binary)):
                if binary[j] == '1':
                    tmp.append(nums[j])
            r.append(tmp)
        return r
