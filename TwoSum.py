class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i]+nums[x] == target:
                    soln = [i, x]
                    return soln
            
def main():
	test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	target = 3

	solution = Solution()

	print("List:", test, "\nTarget: ", target, "\nAnswer:", solution.twoSum(test, target))

if __name__ == "__main__":
	main()