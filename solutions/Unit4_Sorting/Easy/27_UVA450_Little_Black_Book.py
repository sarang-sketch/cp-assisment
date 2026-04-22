# UVA 450 - Little Black Book
# https://onlinejudge.org/external/4/450.pdf
#
# Read department entries, parse CSV records, sort all entries by
# last name then first name, print formatted output with separators.

import sys

def solve():
    n = int(input())
    entries = []
    
    for _ in range(n):
        input()  # blank line separator
        dept = input().strip()
        while True:
            try:
                line = input().strip()
            except EOFError:
                break
            if not line:
                break
            parts = line.split(',')
            if len(parts) < 7:
                break
            title = parts[0]
            first = parts[1]
            last = parts[2]
            address = parts[3]
            home_phone = parts[4]
            work_phone = parts[5]
            campus_box = parts[6]
            entries.append((last, first, title, address, dept, home_phone, work_phone, campus_box))
    
    # Sort by last name, then first name (case-insensitive)
    entries.sort(key=lambda e: (e[0].lower(), e[1].lower()))
    
    for entry in entries:
        last, first, title, address, dept, home_phone, work_phone, campus_box = entry
        print('-' * 40)
        print(f"{title} {first} {last}")
        print(address)
        print(f"Department: {dept}")
        print(f"Home Phone: {home_phone}")
        print(f"Work Phone: {work_phone}")
        print(f"Campus Box: {campus_box}")
    print('-' * 40)

if __name__ == "__main__":
    solve()
