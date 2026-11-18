class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # I get the queue idea, I think:
        #   - build the queue starting from 0 to k-1.
        dq = deque()
        r = 0
        res = []
        while r < k:
            if len(dq) == 0:
                dq.append(r)
            else:
                while dq and nums[dq[0]] < nums[r]:
                    dq.popleft()
                dq.appendleft(r)
            r += 1
        left = 1
        exitingIndex = left - 1
        right = k
        res.append(nums[dq[-1]])
        # The subsequent loop has to start the shifting.
        while right < len(nums):
            # remove the leftmost index.
            if exitingIndex == dq[-1]:
                dq.pop()
            while dq and nums[dq[0]] < nums[right]:
                dq.popleft()
            dq.appendleft(right)
            left += 1
            exitingIndex = left - 1
            right += 1
            res.append(nums[dq[-1]])
        return res
