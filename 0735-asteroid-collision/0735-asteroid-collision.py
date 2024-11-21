class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                sum_=a+stack[-1]
                if sum_<0:
                    stack.pop()
                elif sum_>0:
                    a=0
                    break
                else:
                    stack.pop()
                    a=0
            if a!=0:
                stack.append(a)
        return stack
        