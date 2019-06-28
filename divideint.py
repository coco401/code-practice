class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         positive = (dividend < 0) == (divisor < 0)
#         a, b, res = abs(dividend), abs(divisor), 0

#         while a >= b:
#             x = 0
#             while a >= b << x + 1: x += 1
#             res += 1 << x
#             a -= b << x
        
        
#         if not positive:
#             res = -res
#         return min(max(-2**32, res), 2**31 - 1)
    
    
    def divide(self, A, B):
        if (A == -2147483648 and B == -1): 
            return 2147483647
        
        a, b, res = abs(A), abs(B), 0
        for shift in range(32)[::-1]:
            if a >= b << shift:
                res += 1 << shift
                a -= b << shift        
        return res if (A > 0) == (B > 0) else -res

if __name__ == "__main__":
    sol, A, B = Solution(), 10, -3
    print(sol.divide(A, B))
