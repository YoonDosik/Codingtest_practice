def solution(food):
    for i in range(len(food)):

        if food[i] % 2 != 0:
            food[i] -= 1

    num = {(str(i)): int(count / 2) for i, count in enumerate(food)}

    result = ""
    for i in num:
        result += i * num[i]

    return result + '0' + result[::-1]
