def solution(id_pw, db):
    dic = {}
    for i, j in db:
        dic[i] = j

    if id_pw[0] in dic:
        if dic[id_pw[0]] == id_pw[1]:
            return 'login'
        if dic[id_pw[0]] != id_pw[1]:
            return 'wrong pw'
    else:
        return 'fail'