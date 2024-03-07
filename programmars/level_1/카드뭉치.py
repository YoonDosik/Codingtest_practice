from collections import deque

# card1과 card2로 부터 무엇을 먼저 뽑아야할지 조합을 찾는게 아닌 goal의 결과 비교를 수행함
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    answer = []

    for word in goal:
        if len(cards1) > 0 and word == cards1[0]:
            answer.append(cards1.popleft())
        if len(cards2) > 0 and word == cards2[0]:
            answer.append(cards2.popleft())

    if answer == goal:
        return 'Yes'
    else:
        return 'No'


