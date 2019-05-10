class Solution:
    def reverse(self, x):
        number = x
        reversed_num = 0
        num_flag = 1

        if x*-1 > 0:
            num_flag = -1
            number*=-1

        counter = len(str(number))-1
        
        while (number >= 1):
            reversed_num = reversed_num + (int(number%10)*(10**counter))
            if reversed_num > (2**31 - 1):
                return 0
            number/=10
            counter-=1
        
        reversed_num*=num_flag
        return reversed_num

def main():
    test_num = [321, -321, 9999999999999999999999999999999999, 83]

    solution = Solution()

    print("Input Numbers: ", test_num[0], test_num[1], test_num[2], test_num[3], "\nAnswers:", solution.reverse(test_num[0]), solution.reverse(test_num[1]), solution.reverse(test_num[2]), solution.reverse(test_num[3]))
    #print(solution.reverse(test_num[1]))

if __name__ == "__main__":
    main()