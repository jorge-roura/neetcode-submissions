class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
                i = 0;
                pop = 0;
                while i < len(nums) -1:
                        sum = target - nums[i]
                        nums.pop(i)
                        pop += 1
                        if sum in nums and nums.index(sum) != i - pop:
                                return [pop-1, nums.index(sum) + pop];
                return False;
