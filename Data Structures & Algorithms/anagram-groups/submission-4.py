class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        myMap = {}

        for word in strs:
            count = {}

            for char in word:
                count[char] = 1 + count.get(char, 0)

            key = frozenset(count.items())

            if key not in myMap:
                myMap[key] = []

            myMap[key].append(word)

        return list(myMap.values())


strs = ["act", "tops", "cat", "stop", "hat"]
sol = Solution()

print(sol.groupAnagrams(strs));

