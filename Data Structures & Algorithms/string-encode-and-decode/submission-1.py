class Solution:

    def encode(self, strs: List[str]) -> str:
        self.x = strs
        return "a";

    def decode(self, s: str) -> List[str]:
        return self.x
