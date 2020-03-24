from typing import List


class Solution:

  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []

    count = 0
    take = nums[0]
    other = nums[1:]

    while count < len(nums):
      count += 1
      # generate ans as below

    return ans


my = Solution()
n = [1, 2, 3]
ans = my.permute(n)
nAns = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print("ans", ans, ans=nAns)

# 1, 2, 3

# 0, 1, 2

# 0, 1, 2
# 0 = [1, 2]
# 0, 1
# 0, 2
# 1 = [0, 2]
# 1, 0
# 1, 2
# 2 = [1, 3]
# 2, 0
# 2, 1
