class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Step 1: Handle the empty array case
        if not nums:
            return 0
        
        # Step 2: The 'Anchor' (Slow Pointer)
        # It starts at 0 because the first element is always unique.
        i = 0
        
        # Step 3: The 'Scout' (Fast Pointer)
        # It starts at 1 and scans every element to the end.
        for j in range(1, len(nums)):
            
            # Step 4: Compare Scout with Anchor
            if nums[j] != nums[i]:
                # If they are different, we found a new unique number!
                # Move the Anchor forward to the next empty 'slot'
                i += 1
                # Copy the Scout's new number into that slot
                nums[i] = nums[j]
        
        # Step 5: Return k (the count of unique elements)
        # Since i is an index (starting at 0), the count is i + 1.
        return i + 1