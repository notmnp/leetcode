class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 2 hashmaps
        # hashmap1 = {sortedWord: indice}
        # hashmap2 = {string: occurances}

        anagrams = {}
        sortedArray = []

        for i in range(len(strs)):


            s = "".join(sorted(strs[i]))

            if s not in anagrams:
                anagrams[s] = len(anagrams)
                sortedArray.append([])

            sortedArray[anagrams[s]].append(strs[i])
        
        return sortedArray


