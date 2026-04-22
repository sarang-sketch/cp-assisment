# UVA 11321 - Sort! Sort!! and Sort!!!
# https://onlinejudge.org/external/113/11321.pdf
#
# Sort n integers with modulus M. Primary key: x % M ascending.
# If x % M equal: odd numbers come before even numbers.
# If same parity: odd numbers descending, even numbers ascending.
# Note: the problem uses C-style modulus (can be negative for negative numbers).

import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx]); m = int(input_data[idx + 1])
        idx += 2
        if n == 0 and m == 0:
            print("0 0")
            break
        
        nums = []
        for i in range(n):
            nums.append(int(input_data[idx]))
            idx += 1
        
        def sort_key(x):
            mod = x % m  # Python mod (always non-negative for positive m)
            # We need C-style mod which preserves sign
            if x < 0 and x % m != 0:
                mod = x % m - m  # C-style: e.g., -7 % 3 = -1 in C
            is_odd = x % 2 != 0
            # Primary: mod ascending
            # Secondary: odd before even (odd=0, even=1)
            # Tertiary: odd descending, even ascending
            if is_odd:
                return (mod, 0, -x)
            else:
                return (mod, 1, x)
        
        nums.sort(key=sort_key)
        print(f"{n} {m}")
        for x in nums:
            print(x)
        
    print("0 0") if False else None  # already printed

if __name__ == "__main__":
    solve()
