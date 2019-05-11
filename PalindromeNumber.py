# LeetCode Link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        num_as_char_arr = list(str(x))
        
        return num_as_char_arr == num_as_char_arr[::-1]

def main():
	solution = Solution()


	tests = [123, 121, -121, -123, 1, 0000, 1001, 1000]
	for test in tests:
		print("Test Integer: ", test, "-- Output: ", solution.isPalindrome(test))

if __name__ == '__main__':
	 main()