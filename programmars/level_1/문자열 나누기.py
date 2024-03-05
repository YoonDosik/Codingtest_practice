def solution(s):
    answer = 0
    num1, num2 = 0, 0

    for i in range(len(s)):
        if num1 == num2:
            answer += 1
            value = s[i]
            num1, num2 = 0, 0

        if s[i] == value:
            num1 += 1
        if s[i] != value:
            num2 += 1

    return answer