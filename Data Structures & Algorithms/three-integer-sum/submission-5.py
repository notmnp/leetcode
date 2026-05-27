class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        s = sorted(nums)
        output = []
        
        for i in range(len(nums)-2):

            l = i+1
            r = len(nums)-1

            # if i != 0 and s[i] == s[i-1]:
            #     print(i)
            #     print(s)
            #     continue

            while l < r:
                if s[i] + s[l] + s[r] < 0 and l < r:
                    l += 1
                elif s[i] + s[l] + s[r] > 0 and l < r:
                    r -= 1
                else: 
                    if sorted([s[i],s[l],s[r]]) not in output: 
                        output.append(sorted([s[i],s[l],s[r]]))
                    l += 1
                    r -= 1
                
        return output