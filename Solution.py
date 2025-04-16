from collections import defaultdict
                                                                        # By Coding Moves
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        left = 0
        pair_count = 0
        result = 0

        for right in range(len(nums)):
            # Add new element to frequency map and update pair count
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1

            # Shrink window from the left as long as we have enough pairs
            while pair_count >= k:
                # Count how many valid subarrays start at left and end at or after right
                result += len(nums) - right

                # Remove nums[left] from window and update pair count
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]
                left += 1

        return result

        
