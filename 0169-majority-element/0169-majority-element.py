class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 # get the value of key num if is dosent exit return 0  
        
        ##max_count = max(countArray)
        ##majority_element = countArray.index(max_count)
        majority_element = max(counts, key=counts.get)
    

        return majority_element

            

