def solution(s):
    answer = []
    dic = {}
    for i, value in enumerate(s):
        if value not in dic:
            dic[value] = i
            answer.append(-1)
        else:
            answer.append(i - dic[value])
            dic[value] = i
    return answer