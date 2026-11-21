class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            lens = int(s[i:j])

            decoded.append(s[j+1:j+lens+1])

            i = j + lens + 1

        return decoded