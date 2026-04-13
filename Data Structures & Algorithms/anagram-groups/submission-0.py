class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #key is the frequency array, value is all words which share that frequency array

        group_anagrams = dict()
        for word in strs:
            key = tuple(convert_to_freq_array(word))
            if key in group_anagrams:
                group_anagrams[key].append(word)
            else:
                group_anagrams[key] = [word]
        return list(group_anagrams.values())

def convert_to_freq_array(word):
    freq_array = [0] * 26
    for c in word:
        freq_array[ord(c) - 97] += 1
    return freq_array
    

        





        