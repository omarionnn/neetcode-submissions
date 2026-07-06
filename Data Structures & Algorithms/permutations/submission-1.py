class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.perm = []
        self.pick = [False] * len(nums)
        

        self.backtrack(self.perm, self.pick, nums)
        return self.output


    def backtrack(self, perm, pick, nums):
        if len(perm) == len(nums):
            self.output.append(perm.copy())
            return 


        for i in range(len(nums)):
            if not pick[i]:
                self.perm.append(nums[i])
                self.pick[i] = True
                self.backtrack(perm, pick, nums)
                self.perm.pop()
                self.pick[i] = False