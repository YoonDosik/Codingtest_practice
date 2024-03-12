def solution(arr):
    answer = []
    for i, value in enumerate(arr):
        if i == 0:
            answer.append(value)
        else:
            if answer[-1] != value:
                answer.append(value)
    return answer