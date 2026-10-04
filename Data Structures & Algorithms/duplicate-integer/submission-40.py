
#class Solution:
#    def hasDuplicate(self,nums):
#        n = len(nums)
#        s = len(set(nums));
#        if n == s:
#                return False;
#        return True;

class Solution:
    def hasDuplicate(self,nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
