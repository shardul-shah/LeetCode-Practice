# LeetCode Link: https://leetcode.com/problems/longest-common-prefix/
# FIXME: FUTURE GOAL: Simplify code even more to use only 1 for loop and keeping track of the index at which the common prefix changes...
# ... seems to be a simpler solution.

class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""

        old_common_prefix = list(strs[0])
        
        for i in range(0, len(strs)):
            new_common_prefix = []
            for j in range(0, min(len(old_common_prefix), len(list(strs[i])))):
                if old_common_prefix[j] == list(strs[i])[j]:
                    new_common_prefix.append(list(strs[i])[j])
                else:
                    break
            if new_common_prefix == []:
                return ""
            old_common_prefix = new_common_prefix

        return "".join(new_common_prefix)
                            
def main():
    solution = Solution()
    examples = []
    examples.append(["flower", "flow", "flight"])
    examples.append(["aca", "cba"])
    examples.append([])
    examples.append([""])
    examples.append(["", "", ""])
    examples.append(["flow", "flow"])
    examples.append(["bus", "buskun", "b"])

    for example in examples:
        print("Example: ", example, "Solution: ", solution.longestCommonPrefix(example))

if __name__ == '__main__':
    main()