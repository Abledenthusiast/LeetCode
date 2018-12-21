class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_val = max(A)
        min_val = min(A)
        res = 0
        if K <= 0:
            res = max_val - min_val
        else:
            max_dif = max_val - K
            min_dif = min_val + K
            res = max_dif - min_dif
        
        if res < 0:
            res = 0
        return res
        
        
    