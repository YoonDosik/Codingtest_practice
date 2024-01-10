def solution(t, p):
    length = len(p)
    max_length = len(t)

    result = 0
    for i in range(length, max_length + 1):
        if t[i - length:i] <= p:
            result += 1
    return result

