class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)

        while i < n:
            if nums[i] == val:
        # Overwrite the current bad element with the last good one
                n -= 1
                nums[i] = nums[n]
            else:
                # Keep moving forward if the element is fine
                i += 1
        return n
