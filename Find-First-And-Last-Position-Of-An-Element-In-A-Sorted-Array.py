class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return [-1, -1]
        first = self.binarysearch(nums, target, True)
        last = self.binarysearch(nums, target, False)
        return [first, last]
    
    def binarysearch(self, nums, target, last):
        low, high = 0, len(nums)-1
        while low<=high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                if last!=False:
                    if mid == 0 or nums[mid] > nums[mid - 1]:
                        return mid
                    else:
                        high = mid - 1
                    
                else:
                    if mid == len(nums) - 1 or nums[mid] < nums[mid+1]:
                        return mid
                    else:
                        low = mid + 1
            
            elif nums[mid] > target:
                high = mid - 1
                
            else:
                low = mid + 1
        
        return -1
