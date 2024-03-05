def solution(babbling):
    Words = ['aya', 'ye', 'woo', 'ma']
    answer = 0

    for element in babbling:
        for word in Words:
            if word * 2 not in element:
                element = element.replace(word, ".")

        element = element.replace('.', "")
        if len(element) == 0: # same if not element.strip()
            answer += 1

    return answer