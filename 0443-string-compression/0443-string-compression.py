
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        index = 0

        while i < n:
            curr = chars[i]
            count = 0

            # Find count of duplicates
            while i < n and chars[i] == curr:
                i += 1
                count += 1

            # Assign current character
            chars[index] = curr
            index += 1

            # Add the count if greater than 1
            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[index] = ch
                    index += 1

        return index
