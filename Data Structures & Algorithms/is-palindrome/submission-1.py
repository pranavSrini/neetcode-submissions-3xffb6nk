class Solution:
    def isPalindrome(self, s: str) -> bool:



        l = 0
        r = len(s) - 1
        s = s.lower()

        while(l < r):

            left = ''
            right = ''
            if(s[l].isalpha() or s[l].isdigit()):
                left = s[l]
            else:
                l+=1
            if(s[r].isalpha() or s[r].isdigit()):
                right = s[r]
            else:
                r-=1

            if(len(left) > 0 and len(right) > 0):
                if(left == right):
                    l+=1
                    r-=1 
                else:
                    return False               


        return True

        