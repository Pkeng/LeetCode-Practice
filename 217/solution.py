class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)<2):
            return False
        if(len(set(nums)) < len(nums)):
            return True
        return False


if __name__ == "__main__":
    nums = [2, 7, 2, 15]
    assert (Solution().containsDuplicate(nums) == True)
    nums = [3, 2, 4]
    assert (Solution().containsDuplicate(nums) == False)