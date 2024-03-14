def solution(numbers, target):
    result = [0]
    for num in numbers:
        mid = []
        for i in result:
            mid.append(i + num)
            mid.append(i - num)
        result = mid

    return result.count(target)

