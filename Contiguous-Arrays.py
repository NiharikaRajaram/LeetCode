class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        hashmap = {0:-1}
        rsum, mlen = 0, 0
        
        for i in range(0, len(nums)):
            # find rsum
            rsum = rsum+1 if nums[i] == 0 else rsum-1
            # check if rsum exists in hashmap
            if rsum in hashmap:
                # calculate max length
                mlen = max(mlen, i - hashmap.get(rsum))
            else:
                hashmap[rsum] = i
                
        return mlen
