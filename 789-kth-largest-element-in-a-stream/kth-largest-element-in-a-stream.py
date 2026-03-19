class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.array = nums[-k:]   # keep k largest elements

    def add(self, val: int) -> int:
        self.array.append(val)
        self.array.sort()

        # keep only k largest
        if len(self.array) > self.k:
            self.array.pop(0)   # remove smallest

        return self.array[0]    # kth largest


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)