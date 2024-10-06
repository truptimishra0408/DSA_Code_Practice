class Solution:
    def checkValidString(self, s: str) -> bool:
        open_st = []
        asterisks_st = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_st.append(i)
            elif ch == '*':
                asterisks_st.append(i)
            else:
                if open_st:
                    open_st.pop()
                elif asterisks_st:
                    asterisks_st.pop()
                else:
                    return False

        # Post-processing for unmatched '('
        while open_st and asterisks_st:
            if open_st[-1] > asterisks_st[-1]:
                return False
            open_st.pop()
            asterisks_st.pop()

        return not open_st

        