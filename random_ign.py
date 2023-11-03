import random as ran


start = int('AC00', 16)
end = int('D7A3', 16)


def random_ign(length):
    for i in range(length):
        print(chr(ran.randint(start, end)), end='')

random_ign(2)

cho_list = list(range(0x1100, 0x1113))  # ㄱ ~ ㅎ
jung_list = list(range(0x1161, 0x1176))  # ㅏ ~ ㅣ
jong_list = list(range(0x11A8, 0x11C3))  # (없음) ~ ㅎ

print(list(map(chr, cho_list)))
print(jung_list)
print(list(map(chr, jong_list)))

for cho in cho_list:
    for jung in jung_list:
        for jong in jong_list:
            character = chr(cho) + chr(jung)
            if jong != 0x11A7:  # (중성만 있는 경우)
                character += chr(jong)
            print(character, end=' ')