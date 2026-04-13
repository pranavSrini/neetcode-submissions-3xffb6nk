class Solution:

    def encode(self, strs: List[str]) -> str:

        # if its an integer, read integer more characters
        #once you hit another integer(which you inevitably should)
        # stop, thats a string
        #what if there are numbers IN the string?
        #there isnt a unique symbol we can use as a delimiter
        #instead, we need a different method of representation
        #

        encoded = ""

        if not strs:
            return ""

        for s in strs:
            encoded += (str(len(s)) + "#" + s)
        
        print(encoded)
        
        return encoded





    def decode(self, s: str) -> List[str]:

        if s == "":
            return []

        i = 0
        sol = []

        while(i < len(s)):

            j = i

            while(s[j] != '#'):

                j+=1
            
            size = int(s[i:j])
            i = j + 1
            sol.append(s[i:i + size])
            i += size

        return sol


            

        