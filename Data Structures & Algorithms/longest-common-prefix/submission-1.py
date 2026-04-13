class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest = len(min(strs, key=len))

        prefix = ''

        for c_i in range(shortest):

            for i in range(1, len(strs)):

                if(strs[i - 1][c_i] != strs[i][c_i]):

                    return prefix
                
            prefix += strs[0][c_i]
        
        return prefix



                



         
        