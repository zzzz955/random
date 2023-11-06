import random as ran


def create_random_ign(cho, jung, jong, digit):
    nick_name = ''
    if jong:
        for i in range(digit):
            char = ran.choice(cho) + ran.choice(jung) + ran.choice(jong)
            nick_name += char
    else:
        for i in range(digit):
            char = ran.choice(cho) + ran.choice(jung)
            nick_name += char
    return nick_name

