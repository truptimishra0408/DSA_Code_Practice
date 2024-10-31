def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10
    return total  # Correctly indented return statement

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = sum_of_squares(slow)  # Move slow pointer
            fast = sum_of_squares(sum_of_squares(fast))  # Move fast pointer
            
            if slow == 1:  # If slow pointer reaches 1, it's a happy number
                return True
            if slow == fast:  # If they meet, there's a cycle (not a happy number)
                return False
