class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        if set(word1)!=set(word2):
            return False
        def get_frequency(word):
            freq={}
            for char in word:
                if char in freq:
                    freq[char]+=1
                else:
                    freq[char]=1
            
            return freq
        freq1=get_frequency(word1)
        freq2=get_frequency(word2)

        return sorted(freq1.values())==sorted(freq2.values())


        