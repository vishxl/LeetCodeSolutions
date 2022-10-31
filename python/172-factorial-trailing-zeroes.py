class Solution:
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result

if __name__ == "__main__":
    print Solution().trailingZeroes(100)