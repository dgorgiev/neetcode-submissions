class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        def rec(right: str):
            if not right:
                return

            slen = ""
            for c in right:
                if c == "#":
                    break
                slen = slen + c
            lenslen = len(slen)
            slen = int(slen)

            decoded.append(right[lenslen+1:lenslen + slen+1])
            rec(right[lenslen+slen+1:])

        rec(s)
        return decoded