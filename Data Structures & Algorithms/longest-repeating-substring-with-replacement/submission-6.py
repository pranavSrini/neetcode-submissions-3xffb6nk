class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #empty string case
        if s is None: return 0


        #identify the k + 1 largest 


        #approach 1: naive algo

        #for every letter, compute size and location of islands/runs
        # for each island, check if the gap between the island and the next one
        # is < k. of those
        # return max letter_sum

        #dead end - cant join islands greedily

        #approach 2: two pointers 
        # for each letter , find the largest window that starts and ends with that letter
        # that has <= k other letters, use frequency array to check

        #implementation
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #the answer
        max_max_window = 0

        #for each letter in alphabet
        for c in alphabet:

            #go through string

            #dont us frequency array to check-must be a better way
            #use pointers to control allowed k

            #only need to check the whole string once??

            #move left & forward if we are not yet at an instance of the letter?
            #once we get there, 
                # right = left
            # move right forward(begin window) whilst allowed <= c
            # all of these letters can be replaced
            # stop right when allowed is hit
                # max_window = max(max_window, right - left + 1)
                # left = right
                # allowed = 0
            
            #repeat

            #outer loop condition go until we hit the end of the string

            left = 0
            right = 0

            #keep track of letters != c
            allowed = 0

            #the largest window for the current letter
            max_window_len = 0

            print(c)
            print()

            while(right < len(s)):

                if(s[right] != c):

                    allowed += 1
                
                if(allowed <= k):

                    max_window_len = max(max_window_len, right - left + 1)

                else:

                    if(s[left] != c):

                        allowed -= 1

                    left += 1
                
                right += 1
            
            max_max_window = max(max_window_len, max_max_window)
        
        return max_max_window


                
                













            





        