class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <= 0:
            return []
        num_map = { '2': 'abc', '3':'def','4': 'ghi', '5': 'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            
        n = 0
        result = []
        self.used = {}
        return self.permute_digits(digits, num_map, "", result, n )
                
            
    def permute_digits(self, digits, num_map, mapped_str, result, n):
        
        
        if len(digits) == len(mapped_str):
            result.append(mapped_str)
            return

        for i in range(0, len(num_map[digits[n]])):
            #if not num_map[int(digits[n])][i] in self.used:         
            mapped_str += num_map[digits[n]][i]
            self.permute_digits(digits, num_map, mapped_str, result, n+1)
            mapped_str =  mapped_str[:-1]
        return result

