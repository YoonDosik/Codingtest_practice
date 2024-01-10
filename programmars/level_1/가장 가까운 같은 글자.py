def solution(s):
    answer = []
    result = {}
    for i, value in enumerate(s):
        if value in result:
            answer.append(i - result[value])
            result[value] = i
        else:
            answer.append(-1)
            result[value] = i

    return answer