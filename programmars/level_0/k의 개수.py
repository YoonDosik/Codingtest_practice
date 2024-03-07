def solution(i, j, k):
    answer = 0
    for value in range(i,j+1):
        for ele in list(str(value)):
            if str(k) in ele:
                answer += 1
    return answer