# UVA 10194 - Football (aka Soccer)
# https://onlinejudge.org/external/101/10194.pdf
#
# Parse match results, compute team standings, sort by multiple criteria.

import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    n = int(data[idx].strip()); idx += 1
    
    first = True
    for _ in range(n):
        if not first:
            print()
        first = False
        
        tournament = data[idx].strip(); idx += 1
        t = int(data[idx].strip()); idx += 1
        
        teams = {}
        for i in range(t):
            name = data[idx].strip(); idx += 1
            teams[name] = {
                'points': 0, 'games': 0, 'wins': 0, 'ties': 0, 'losses': 0,
                'gf': 0, 'ga': 0, 'name': name
            }
        
        g = int(data[idx].strip()); idx += 1
        for _ in range(g):
            line = data[idx].strip(); idx += 1
            # Format: team1#goals1@goals2#team2
            parts = line.split('#')
            team1 = parts[0]
            mid = parts[1].split('@')
            goals1 = int(mid[0])
            goals2_team2 = mid[1].split('#', 1) if '#' in mid[1] else mid[1].split('#')
            # Actually: parts = [team1, "goals1@goals2", team2]
            goals2 = int(parts[1].split('@')[1])
            goals1 = int(parts[1].split('@')[0])
            team2 = parts[2]
            
            teams[team1]['games'] += 1
            teams[team2]['games'] += 1
            teams[team1]['gf'] += goals1
            teams[team1]['ga'] += goals2
            teams[team2]['gf'] += goals2
            teams[team2]['ga'] += goals1
            
            if goals1 > goals2:
                teams[team1]['wins'] += 1
                teams[team1]['points'] += 3
                teams[team2]['losses'] += 1
            elif goals1 < goals2:
                teams[team2]['wins'] += 1
                teams[team2]['points'] += 3
                teams[team1]['losses'] += 1
            else:
                teams[team1]['ties'] += 1
                teams[team2]['ties'] += 1
                teams[team1]['points'] += 1
                teams[team2]['points'] += 1
        
        # Sort teams
        team_list = list(teams.values())
        team_list.sort(key=lambda x: (
            -x['points'],
            -x['wins'],
            -(x['gf'] - x['ga']),
            -x['gf'],
            -x['games'],  # fewer games is better (but problem says most games)
            x['name'].lower()
        ))
        
        print(tournament)
        for i, team in enumerate(team_list):
            gd = team['gf'] - team['ga']
            print(f"{i+1}) {team['name']} {team['points']}p, {team['games']}g ({team['wins']}-{team['ties']}-{team['losses']}), {gd}gd ({team['gf']}-{team['ga']})")

if __name__ == "__main__":
    solve()
