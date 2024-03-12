from collections import deque


def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    queue = deque(queue)
    result = []
    while queue:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            result.append(cur)

    for i in result:
        if i[0] == location:
            return result.index(i) + 1