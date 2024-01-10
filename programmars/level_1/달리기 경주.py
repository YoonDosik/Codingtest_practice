def solution(players, callings):
    idx = {player: i for i, player in enumerate(players)}

    for i in callings:
        # 현재 호명 등수
        index = idx[i]
        idx[i] -= 1
        idx[players[index - 1]] += 1

        players[index - 1], players[index] = players[index], players[index - 1]

    return players