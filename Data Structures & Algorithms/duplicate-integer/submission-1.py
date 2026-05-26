class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # key = number, value = occurances
        total = {}

        for i in range(len(nums)): 
            if total.get(nums[i]):
                total[nums[i]] += 1
            else: 
                total[nums[i]] = 1

        print(total)

        for value in total.values(): 
            if value > 1:
                return True
        return False