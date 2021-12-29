class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        
        for num in nums1:
            s.add(num)
        
        intersection = set()
        
        for num in nums2:
            if num in s:
                intersection.add(num)
                
        return list(intersection)
