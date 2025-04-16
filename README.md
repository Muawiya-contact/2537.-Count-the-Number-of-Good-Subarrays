# 🚀 LeetCode 2537 - Count the Number of Good Subarrays

## 💡 Problem Description

Given an integer array `nums` and an integer `k`, return the number of **good subarrays** of `nums`.

A subarray `arr` is **good** if there are **at least `k` pairs** of indices `(i, j)` such that `i < j` and `arr[i] == arr[j]`.

A subarray is a **contiguous non-empty sequence** of elements within an array.

---

### 🧪 Examples

**Example 1:**
### Input: 
nums = [1,1,1,1,1], k = 10
### Output:
 1
### Explanation:
The only good subarray is the entire array.

---

### ✅ Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^9`

---

## 🧠 Approach

We use a **sliding window** + **hash map** to efficiently count pairs within a window.  
For each window, we maintain a count of how many valid pairs it has.  
If the number of pairs is at least `k`, all subarrays ending at the current `right` index and starting from current `left` or after are **good**.

This approach ensures a **linear time complexity O(n)**.

---

## 👨‍💻 Python Code

```python
from collections import defaultdict

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
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1

            while pair_count >= k:
                result += len(nums) - right
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]
                left += 1

        return result
```
## 📺 Video Explanation & More
## 📌 Watch on @Coding_Moves – your hub for coding tips, algorithm tricks, and AI projects!
## 🔔 Subscribe and join the journey to becoming a top-tier programmer.

#📬 Contact
+ Made with ❤️ by @Coding_Moves
+ Let's connect and grow together as coders!
