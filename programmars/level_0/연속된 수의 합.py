def solution(num, total):
    # 정답에 음수부터 시작하는 값이 있어 -부터 시작함
    for i in range(-num, 101):
        answer = 0
        for j in range(num):
            answer += (i + j)
        if answer == total:
            result = [i + j for j in range(num)]
            return result
