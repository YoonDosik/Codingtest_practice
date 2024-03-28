def solution(people, limit):
    people.sort()
    print(people)

    a = 0
    b = len(people) - 1

    answer = 0
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            answer += 1
        b -= 1

    return len(people) - answer