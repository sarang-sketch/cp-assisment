# UVA 11777 - Automate the Grades
# https://onlinejudge.org/external/117/11777.pdf
#
# Calculate total: Term1 + Term2 + Final + Attendance + avg(best 2 of 3 class tests).
# Grade: A>=90, B>=80, C>=70, D>=60, F<60.

import sys

def solve():
    t = int(input())
    for case in range(1, t + 1):
        vals = list(map(int, input().split()))
        term1, term2, final, attend = vals[0], vals[1], vals[2], vals[3]
        tests = sorted(vals[4:7], reverse=True)
        class_test = (tests[0] + tests[1]) / 2.0
        total = term1 + term2 + final + attend + class_test
        
        if total >= 90:
            grade = 'A'
        elif total >= 80:
            grade = 'B'
        elif total >= 70:
            grade = 'C'
        elif total >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Case {case}: {grade}")

if __name__ == "__main__":
    solve()
