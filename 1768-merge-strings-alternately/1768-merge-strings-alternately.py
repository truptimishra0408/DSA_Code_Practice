class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        merged_string=[]
        while i<len(word1) and j<len(word2):
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i+=1
            j+=1
        if i<len(word1):
            merged_string.append(word1[i:])
        if j<len(word2):
            merged_string.append(word2[j:])
        return ''.join(merged_string)

        