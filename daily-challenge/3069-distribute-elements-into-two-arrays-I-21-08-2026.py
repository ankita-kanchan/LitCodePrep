class Solution:
    """
    LeetCode 3069 - Distribute Elements Into Two Arrays I

    Approach:
    - Put the first element in arr1 and second in arr2.
    - For each remaining element:
        - If last element of arr1 > last element of arr2,
          add the element to arr1.
        - Otherwise, add it to arr2.
    - Return arr1 + arr2.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def resultArray(self, nums):
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2