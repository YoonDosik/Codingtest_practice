import heapq

def solution(scovile, K):
    heapq.heapify(scovile)

    answer = 0

    while scovile[0] < K:

        if len(scovile) == 1:
            return -1

        min1 = heapq.heappop(scovile)
        min2 = heapq.heappop(scovile)
        mix_scovile = min1 + (min2 * 2)

        heapq.heappush(scovile, mix_scovile)
        answer += 1

    return answer

