
class solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return([i, j])
            
solution = solution()
nums = [2, 11, 15, 7]
target = 9
print(solution.twoSum(nums, target))
