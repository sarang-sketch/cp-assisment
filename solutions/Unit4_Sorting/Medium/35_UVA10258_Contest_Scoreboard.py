# UVA 10258 - Contest Scoreboard
# https://onlinejudge.org/external/102/10258.pdf
#
# ACM-ICPC style scoreboard. For each contestant:
# - number of problems solved (descending)
# - total penalty time (ascending)
# - contestant number (ascending) for tiebreak
# Penalty = sum of accepted problem times + 20 * wrong submissions before acceptance.

import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    cases = int(data[idx].strip()); idx += 1
    
    first_case = True
    for _ in range(cases):
        # Skip blank line
        while idx < len(data) and data[idx].strip() == '':
            idx += 1
        
        # contestants: id -> {problems: {prob: (solved, time, penalty_count)}}
        contestants = {}
        
        while idx < len(data) and data[idx].strip() != '':
            parts = data[idx].strip().split()
            idx += 1
            if len(parts) < 4:
                continue
            
            cid = int(parts[0])
            prob = int(parts[1])
            time = int(parts[2])
            result = parts[3]
            
            if cid not in contestants:
                contestants[cid] = {}
            
            if prob not in contestants[cid]:
                contestants[cid][prob] = {'solved': False, 'time': 0, 'penalty': 0}
            
            info = contestants[cid][prob]
            if info['solved']:
                continue  # already accepted, ignore further submissions
            
            if result == 'C':
                info['solved'] = True
                info['time'] = time
            elif result == 'I':
                info['penalty'] += 1
        
        # Compute scores
        results = []
        for cid, problems in contestants.items():
            solved = 0
            penalty = 0
            for prob, info in problems.items():
                if info['solved']:
                    solved += 1
                    penalty += info['time'] + 20 * info['penalty']
            results.append((cid, solved, penalty))
        
        results.sort(key=lambda x: (-x[1], x[2], x[0]))
        
        if not first_case:
            print()
        first_case = False
        
        for cid, solved, penalty in results:
            print(f"{cid} {solved} {penalty}")

if __name__ == "__main__":
    solve()
