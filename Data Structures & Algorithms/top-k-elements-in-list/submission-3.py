class Solution:
        def topKFrequent(self, nums: List[int], k:int) -> List[int]:
                count={};
                for i in range(len(nums)):
                        count[nums[i]] = 1 + count.get(nums[i], 0);

                freq = [];
                for key, val in count.items():
                        freq.append((-val, key));
                heapq.heapify(freq);

                i = 0;
                topK=[];
                while i < k:
                        topK.append(heapq.heappop(freq))
                        i +=1;

                list2=[];
                for val, key in topK:
                        list2.append(key);

                return list2;
