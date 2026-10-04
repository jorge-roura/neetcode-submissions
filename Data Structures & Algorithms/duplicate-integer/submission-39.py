
class Solution:
    def hasDuplicate(self,nums):
        n = len(nums)
        s = len(set(nums));
        if n == s:
                return False;
        return True;