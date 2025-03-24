class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(1,n+1):
            new_b = b + a
            new_a = b
            b = new_b
            a = new_a
        return b
                