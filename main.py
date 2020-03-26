from typing import List


class Solution:

  def getUniqParis(self, size: int):
    uniq = {}
    for i in range(0, size):
      for j in range(0, size):
        if i == j:
          continue
        one = i
        two = j

        if one > two:
          one, two = two, one

        uniq[str(one) + ' ' + str(two)] = True

    return [[int(num) for num in item.split(' ')] for item in uniq.keys()]

  def swap(self, numsOriginal: List[int], i: int, j: int):
    nums = numsOriginal.copy()

    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

    return nums

  def permuteChanged(self, nums: List[int]) -> List[List[int]]:
    ans = [nums]

    index = 0
    while index < len(nums) * len(nums) / 2:
      for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
          ans.append(self.swap(ans[index], i, j))
      index += 1

    return ans

  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = [nums]

    for i in range(0, len(nums) - 1):

      for one in ans.copy():
        for j in range(i + 1, len(nums)):
          ans.append(self.swap(one, i, j))

    return ans

  # TODO: dfs (wide spread search), path and nums
  # make the path and when reach the leaf => add to ans
  # def dfs()


my = Solution()
n = [1, 2, 3]  # 0
# n = [6, 3, 2, 7, 4, -1]
ans = my.permute(n)
nAns = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# nAns = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print("ans", ans, ans == nAns)

# 1, 2, 3
# 2, 1, 3
# 3, 2, 1

# 2, 3, 1
# 3, 2, 1
# 1, 3, 2
# 2, 1, 3

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
