class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = [0] * 26 
        counts_t = [0] * 26
        for char in s:
            counts_s[ord(char) - 97] += 1
        for char in t:
            counts_t[ord(char) - 97] += 1
        for i in range(len(counts_s)):
            if(counts_s[i] != counts_t[i]):
                return False
        return True

        