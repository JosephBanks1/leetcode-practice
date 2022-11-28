class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #List is not defined as the test cases are provided by LeetCode
        #1 loop through the list
        
        for i in range(len(nums)):
        
        #2 add the second int to the first
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
        #3 check the sum against the target            
        #3.1 if yes then return as output
                if sum == target:
                    return(i, j)
        #3.2 if no then repeat with next int against the first                   
        #if end of list is reached return "no sum found"
                else:
                    print("No Sum Found")

