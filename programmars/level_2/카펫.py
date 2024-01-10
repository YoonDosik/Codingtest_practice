
# 실패한 솔루션 함수 (정확도 76.9/100)

def solution(brown, yellow):
    n = brown + yellow
    result = []
    num = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append([i, int(n / i)])
            if i < int(n / i):
                num.append(i)
    return result[(len(num))]

