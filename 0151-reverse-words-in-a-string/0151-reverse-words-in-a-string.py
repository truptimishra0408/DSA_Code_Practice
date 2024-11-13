class Solution:
    def reverseWords(self, s: str) -> str:
        # Helper function to reverse a portion of the list
        def reverse(i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        # Convert string to list for in-place modifications
        s = list(s)
        n = len(s)
        
        # Step 1: Reverse the entire string
        reverse(0, n - 1)
        
        # Step 2: Reverse each word in the reversed string
        i = 0
        while i < n:
            # Skip any spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
                
            j = i
            # Find the end of the current word
            while j < n and s[j] != ' ':
                j += 1
            
            # Reverse the current word
            reverse(i, j - 1)
            
            # Move to the start of the next word
            i = j
        
        # Convert list back to string and trim leading/trailing spaces
        return ' '.join(''.join(s).split())
