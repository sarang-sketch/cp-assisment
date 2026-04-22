# UVA 11475 - Extend to Palindrome
# https://onlinejudge.org/external/114/11475.pdf
#
# Given a string, find the shortest palindrome that begins with that string.
# Use KMP failure function on reversed(s) + '#' + s to find longest
# palindromic suffix, then append the needed characters.

import sys

def kmp_failure(pattern):
    n = len(pattern)
    fail = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        fail[i] = j
    return fail

def solve():
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        rev = s[::-1]
        # Build: rev + '#' + s, find longest prefix of rev that matches suffix of s
        combined = rev + '#' + s
        fail = kmp_failure(combined)
        # Length of longest palindromic suffix of s
        overlap = fail[-1]
        # Append the remaining reversed prefix
        print(s + rev[overlap:])

if __name__ == "__main__":
    solve()
