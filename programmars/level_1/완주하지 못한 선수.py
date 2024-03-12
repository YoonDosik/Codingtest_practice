def solution(participant, completion):

    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

# zip으로 pariticipant와 completion을 묶어 요소가 같은지 아닌지, collections의 Counter 함수 이용

# from collections import Counter
#
# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]


# remove를 쓰니 테스트 케이스는 다 통과되나 효율성 테스트에서 시간초과가 발생함
def solution(participant, completion):
    answer = ''

    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer += i

    return answer


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in skip:
    print(i)