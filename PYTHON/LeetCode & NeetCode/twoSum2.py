
class solution:
    def twoSum(self, nums, target):
        
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if(complement in num_dict):
                return(num_dict[complement], i)
            
            num_dict[num] = i
            return[i, num]
        
solution = solution()
nums = [2 , 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))