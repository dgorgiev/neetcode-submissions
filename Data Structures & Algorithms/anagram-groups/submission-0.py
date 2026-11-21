class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for word in strs:
            freq = [0] * 26
            for character in word:
                # 'a' == 97 
                # ord('a') - 96 == 1
                index = ord(character) - 97
                freq[index] += 1
            freq = tuple(freq)
            if freq not in d:
                d[freq] = []
            d[freq].append(word)

        return list(d.values())

