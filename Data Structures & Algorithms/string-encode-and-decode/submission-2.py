class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        i = 0
        while i < n:
            j = 0
            while s[i+j] != "#":
                j += 1
            lens = int(s[i:i+j])

            decoded.append(s[i+j+1:i+j+lens+1])

            i = i + j + lens + 1

        return decoded