
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solution = list(list())
        saved = {}
        
        for val in strs:
            sorted_str = ''.join(sorted(val))
            print(sorted_str)
            if sorted_str in saved:
                saved[sorted_str].append(val)
            else:
                saved[sorted_str] = [val]
                
        for key, values in saved.items():
            solution.append(values)
        return solution