class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums == None or len(nums) == 0:
            return False
        n, low, high = len(nums), 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                high-=1
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
