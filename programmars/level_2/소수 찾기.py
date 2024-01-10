def solution(numbers):
    import itertools

    num = []
    for n in numbers:
        num.append(n)

    comb = []
    for i in range(len(num)):
        comb += list(itertools.permutations(num, i + 1))

    # comb 안의 수를 정수로 변환함과 동시에 set에 add 하며 중복된 숫자를 제거함
    comb_numbers = set()
    for i in comb:
        a = ''.join(i)
        # 0,1은 소수가 존재하지 않기에 comb_numbers에 2이상인 숫자만을 add함
        if int(a) > 1:
            comb_numbers.add(int(a))
    result = 0
    for value in comb_numbers:
        count = 0
        for i in range(2, value):
            # 2 ~ value-1의 범위 중 단 하나라도 나누어 떨어지면 소수가 아니기에 break
            if value % i == 0:
                count += 1
                break
            else:
                count += 0
        if count == 0:
            result += 1
    return result