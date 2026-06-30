class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                if(nums.index(temp, i + 1) >= 0):
                    s.append(nums.index(nums[i]))
                    s.append(nums.index(temp, i + 1))
                    break
            except:
                continue
        return s