class Solution:

    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        existing = []
        o = []
        for i in range(len(strs)):
            
            temp = {}
            # anagram dictionary
            for j in range (len(strs[i])):
                if strs[i][j] in temp:
                    temp[strs[i][j]] += 1
                else: 
                    temp[strs[i][j]] = 1

            if temp in existing:
                # if anagram already exists,
                # get index of it and append word to array
                index = existing.index(temp)
                o[index].append(strs[i])
            else: 
                # otherwise append dictionary to list
                # and create new subarray in o
                existing.append(temp)
                o.append([strs[i]])

        return o
