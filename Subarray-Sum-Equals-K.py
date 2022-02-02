class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        hashmap = {0:1}
        count = 0
        sum = 0
        for num in nums:
            sum += num
            
            if (sum - k) in hashmap:
                count += hashmap[sum-k]
            if sum not in hashmap:
                hashmap[sum] = 1
            else:
                hashmap[sum] += 1
                
        return count
