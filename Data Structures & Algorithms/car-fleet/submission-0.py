class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        time = list((target - pos)/spd for pos, spd in cars)
        stack = []

        for t in time:
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
        