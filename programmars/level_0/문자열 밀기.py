# 풀이 1

from collections import deque
def solution(A, B):
    A_list = deque(A)
    B_list = deque(B)
    answer = 0
    for _ in range(len(A_list)):
        if A_list == B_list:
            return answer
        else:
            A_list.rotate(1)
            answer += 1
    return -1

# 풀이 2

def solution(A, B):
    B_list = B * 2
    if A in B_list:
        return B_list.find(A)
    else:
        return -1