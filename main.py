from typing import List


class Solution:

  # Each nums item List should be swaped in 'j' ways and added to ans
  # and after it again and again 'i'-1 times
  # hard to understand why it's working =) ...............
  def permuteWorking(self, nums: List[int]) -> List[List[int]]:
    ans = [nums]

    for i in range(0, len(nums) - 1):
      for one in ans.copy():
        for j in range(i + 1, len(nums)):
          ans.append(self.swap(one, i, j))

    return ans

  # TODO: dfs (wide spread search), path and nums
  # make the path and when reach the leaf => add to ans
  # def dfs()
  def allDFS(self, nums: List[int], path: List[int],
             ans: List[List[int]]) -> List[List[int]]:
    if len(nums) == 0:
      ans.append(path)
      return ans

    # print(nums)
    # print(path)
    # print(ans)

    for i, item in enumerate(nums):
      otherNums = nums[:i] + nums[i + 1:]
      newPath = path + [int(item)]
      # print(i, item, otherNums, newPath)
      self.allDFS(otherNums, newPath, ans)
    # print('___')

    return ans

  def permute(self, nums: List[int]) -> List[List[int]]:
    return self.allDFS(nums, [], [])  # I understand this solution =)
    # return self.permuteWorking(nums) # I didn't understand this solutions =)


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

# Runtime: 32 ms, faster than 95.62% of Python3 online submissions for Permutations.
# Memory Usage: 13.2 MB, less than 80.36% of Python3 online submissions for Permutations.