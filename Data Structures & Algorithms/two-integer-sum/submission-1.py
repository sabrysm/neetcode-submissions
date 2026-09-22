class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = defaultdict(list)
        size = len(nums)

        for i in range(size - 1):
            for j in range(i + 1, size):
                answer[nums[i] + nums[j]] = [i, j]
        
        for key, value in answer.items():
            if key == target:
                return value
        return nums
