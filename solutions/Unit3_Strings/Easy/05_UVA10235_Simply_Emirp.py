# UVA 10235 - Simply Emirp
# https://onlinejudge.org/external/102/10235.pdf
#
# Determine if N is: not prime, prime (but not emirp), or emirp.
# An emirp is a prime whose reverse is also prime AND different from itself.

import sys

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if not is_prime(n):
            print(f"{n} is not prime.")
        else:
            rev = int(str(n)[::-1])
            if rev != n and is_prime(rev):
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")

if __name__ == "__main__":
    solve()
