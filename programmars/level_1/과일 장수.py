def solution(k, m, score):
    score = sorted(score, reverse=True)

    count = 0
    for i in range(0, len(score), m):
        result = score[i:i + m]
        if len(result) == m:
            count += (min(result) * m)

    return count