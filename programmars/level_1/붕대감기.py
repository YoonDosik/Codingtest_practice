def solution(bandage, health, attacks):
    max_health = health
    max_time = attacks[-1][0]

    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]] = i[1]

    t = 0
    count = 0

    while t <= max_time:

        if t in attack_dict:
            health -= attack_dict[t]
            count = 0

            if health <= 0:
                return -1

        else:
            count += 1
            if count < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health += (bandage[1] + bandage[2])
                if health > max_health:
                    health = max_health
                count = 0
        t += 1
    return health