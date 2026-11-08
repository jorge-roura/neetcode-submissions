import math

class Solution:
    def product(self, nums: List[int]) -> int:
        prod = 1;
        for i in nums:
            prod *= i;
        return prod;

    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        arrProd=[];
        if self.product(nums) == 0:
            x = nums.index(0);
            arrProd = [0] * (len(nums)-1)
            nums.pop(x);
            arrProd.insert(x, self.product(nums))
        else:
            prod = self.product(nums);
            for i in nums:
                arrProd.append(math.floor(prod/i));

        return arrProd;
