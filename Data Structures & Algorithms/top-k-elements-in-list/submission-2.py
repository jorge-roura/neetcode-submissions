class Solution:
        def topKFrequent(self, nums: List[int], k:int) -> List[int]:
                count={};
                for i in range(len(nums)):
                        count[nums[i]] = 1 + count.get(nums[i], 0);

                list = [];
                for key, val in count.items():
                        heapq.heappush(list,(val, key));

                while k < len(list):
                        heapq.heappop(list);

                list2=[];
                for value, key in list:
                        list2.append(key);

                return list2;
