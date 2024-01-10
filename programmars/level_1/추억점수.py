def solution(name, yearning, photo):
    answer = []

    value = {value: yearning[k] for k, value in enumerate(name)}

    for i in range(len(photo)):

        count = 0

        for j in photo[i]:
            if j in value:
                count += value[j]
            if j not in value:
                count += 0

        answer.append(count)

    return answer
