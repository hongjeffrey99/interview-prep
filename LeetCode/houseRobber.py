# House Robber

# [2, 3, 2] expect 3
# [1, 2, 3, 1] expect 4

def houseRobber(nums):
    if not nums:
        return 0
    
    firstPass = nums[1:] # Prevents looping between nums[0] and nums[n] - I looked at the hints for this
    secondPass = nums[:-1]
    
    def solve(nums):
        solution = [0 for i in range(len(nums))] # initialize dp array
        solution[0] = nums[0]
        solution[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            solution[i] = max(solution[i - 1], solution[i - 2] + nums[i])
        return solution[-1]
       
    return max(solve(firstPass), solve(secondPass))

print(houseRobber([2,3,2]))
print(houseRobber([1,2,3,1]))

