class Solution:
    def merge(self, num1, m, num2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while i >= 0 and j >= 0:
            if num1[i] > num2[j]:
                num1[k] = num1[i]
                i -= 1
            else:
                num1[k] = num2[j]
                j -= 1
            k -= 1
        
        # Copy remaining elements of num2 if any
        while j >= 0:
            num1[k] = num2[j]
            j -= 1
            k -= 1
