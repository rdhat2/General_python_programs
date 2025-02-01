class Solution:
    @staticmethod
    def number_len_check(num: int) -> None:
        """
        Formats the given number as a string of exactly 9 characters.

        - If the number has fewer than 9 digits, it pads the number with leading zeros on the left.
        - If the number has more than 9 digits, it truncates it to the first 9 digits.
        - If the number has exactly 9 digits, it leaves the number unchanged.

        The result is then printed to the console.
        """
        str_num = str(num)
        if len(str_num) < 9:
            new_str = '0' * (9 - len(str_num)) + str_num  # Adding zeros to the left
        elif len(str_num) > 9:
            new_str = str_num[:9]  # Truncating to 9 characters
        else:
            new_str = str_num  # No changes needed if length is exactly 9
        print(new_str)

if __name__ == "__main__":
    test_numbers = [
        1234567890,        # Expected: 123456789
        123456,            # Expected: 000123456
        1234567890123,     # Expected: 123456789
        98765432109876543210,  # Expected: 987654321
        0,                 # Expected: 000000000
        999999999,         # Expected: 999999999
        123456789,         # Expected: 123456789
        42,                # Expected: 000000042
        1000000000,        # Expected: 100000000
    ]

    for num in test_numbers:
        Solution.number_len_check(num)

## Total Time Complexity: O(k), Space Complexity: O(k)
## Future improvements - exception handling for invalid inputs, optimization for time and space complexity.