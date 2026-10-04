class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len (t):
                        return False;
                countS, countT = {}, {}
                for i in range(len(s)):
                        countS[s[i]] = 1 + countS.get(s[i], 0);
                # What does this do?
                # We are making the key and value at the same time.

                for i in range(len(t)):
                        countT[t[i]] = 1 + countT.get(t[i], 0);

                return countS ==  countT;






s = "heloh"
t = "lehoh"

myobj = Solution();
print(myobj.isAnagram(s, t));
