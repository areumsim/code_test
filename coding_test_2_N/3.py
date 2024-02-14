##### sol. 3 #####
def solution(skills):
    n = len(skills)
    results = [0] * n
    players = list(range(n))

    round_num = 1
    while len(players) > 1:
        next_round_players = []

        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                if skills[players[i]] > skills[players[i + 1]]:
                    results[players[i + 1]] = round_num
                    next_round_players.append(players[i])
                else:
                    results[players[i]] = round_num
                    next_round_players.append(players[i + 1])
            else:  # player odds
                next_round_players.append(players[i])

        players = next_round_players
        round_num += 1

    for player in players:
        results[player] = round_num - 1

    return results
