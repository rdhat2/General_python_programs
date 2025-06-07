class Solution:
    def second_largest_element(self, nums):
        first_greatest = second_greates = float("-inf")

        for num in nums:
            if num > first_greatest:
                second_greates = first_greatest
                first_greatest = num
            elif first_greatest > num > second_greates:
                second_greates = num
        
        return second_greates if second_greates != float("-inf") else -1
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.second_largest_element([8,8,7,5]))