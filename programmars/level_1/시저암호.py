def solution(s, n):
    Upperalpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', "J", "K", "L", 'M', "N", "O", 'P', "Q", 'R', "S", 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    loweralpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    answer = ''
    for i in list(s):
        if i == ' ':
            answer += ' '
        elif i in Upperalpha:
            x = Upperalpha * 2
            answer += x[Upperalpha.index(i) + n]
        elif i in loweralpha:
            x = loweralpha * 2
            answer += x[loweralpha.index(i) + n]

    return answer