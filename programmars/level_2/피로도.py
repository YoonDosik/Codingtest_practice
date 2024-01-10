def solution(k, dungeons):
    import itertools
    comb = list(itertools.permutations(dungeons, len(dungeons)))
    answer = 0
    for i in comb:
        fatigue = k
        count = 0
        for j in range(len(i)):
            if fatigue >= i[j][0]:
                count += 1
                fatigue -= i[j][1]
        if count > answer:
            answer = count
    return answer
