
def solution(answers):
    
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    test_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count_1, count_2, count_3 = 0, 0, 0
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        if test_1[s1] == answers[i]:
            count_1 += 1
        if test_2[s2] == answers[i]:
            count_2 += 1
        if test_3[s3] == answers[i]:
            count_3 += 1

    a = max(count_1, count_2, count_3)
    answer = []
    if count_1 == a:
        answer.append(1)
    if count_2 == a:
        answer.append(2)
    if count_3 == a:
        answer.append(3)

    return answer


def solution(answers):
    num_1 = [1, 2, 3, 4, 5] * 2000
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1400
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    count_1, count_2, count_3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == num_1[i]:
            count_1 += 1
        if answers[i] == num_2[i]:
            count_2 += 1
        if answers[i] == num_3[i]:
            count_3 += 1

    max_value = max([count_1, count_2, count_3])

    result = []

    if count_1 == max_value:
        result.append(1)
    if count_2 == max_value:
        result.append(2)
    if count_3 == max_value:
        result.append(3)

    return result