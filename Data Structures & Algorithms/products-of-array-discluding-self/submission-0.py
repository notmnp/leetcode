class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zeros = []
        output = []

        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else: 
                zeros.append(i)

        # two zeros edge case, return array of all zeros
        if len(zeros) > 1:
            return [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if len(zeros) > 0:
                if i in zeros:
                    output.append(product)
                else:
                    output.append(0)
                    
            else: 
                output.append(int(product/nums[i]))

        return output



