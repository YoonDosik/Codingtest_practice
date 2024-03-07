def Rank(result):
    if result != 1 and result != 0:
        return 7 - result
    if result < 2:
        return 6


def solution(lottos, win_nums):
    corr_count = 0
    zero_count = 0

    for lotto in lottos:
        if lotto in win_nums:
            corr_count += 1

        if lotto == 0:
            zero_count += 1

    max_result = corr_count + zero_count
    min_result = corr_count

    return [Rank(max_result), Rank(min_result)]