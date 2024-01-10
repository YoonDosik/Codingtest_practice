def solution(s, skip, index):
    num = index

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for sk in skip:
        alphabet = alphabet.replace(sk, "")
    result = ""
    for alpha in s:
        result += alphabet[(alphabet.index(alpha) + num) % len(alphabet)]

    return result
