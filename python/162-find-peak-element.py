class Solution:
    def findPeakElement(self, num):
        low, high = 0, len(num) - 1
        
        while low < high:
            mid = low + (high - low) / 2
            if (mid == 0 or num[mid - 1] <= num[mid]) and \
               (mid == len(num) - 1 or num[mid + 1] <= num[mid]):
                return mid
            elif mid > 0 and num[mid - 1] > num[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = low + (high - low) / 2
       
        return low

if __name__ == "__main__":
    print Solution().findPeakElement([1,2,3, 1])