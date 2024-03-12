from collections import deque


def solution(progresses, speeds):
    until_time = []

    for i, value in enumerate(progresses):
        if (100 - value) % speeds[i] == 0:
            until_time.append(int((100 - value) / speeds[i]))
        else:
            until_time.append(int((100 - value) / speeds[i]) + 1)

    until_time = deque(until_time)
    answer = 0
    result = []

    for i in range(len(until_time)):
        a = until_time.popleft()

        if i == 0:
            longtime = a
            answer += 1
        else:
            if longtime >= a:
                answer += 1
            else:
                longtime = a
                result.append(answer)
                answer = 1

    # for문 종료 후 남음 answer result에 append

    result.append(answer)
    return result
