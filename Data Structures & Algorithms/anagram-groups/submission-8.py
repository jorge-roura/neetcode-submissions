class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        myMap = {}

        for word in strs:
            count = {}

            for char in word:
                count[char] = 1 + count.get(char, 0)

            key = frozenset(count.items())

            if key in myMap:
                myMap[key].append(word)
            else:
                myMap[key] = [word]

        return list(myMap.values())
