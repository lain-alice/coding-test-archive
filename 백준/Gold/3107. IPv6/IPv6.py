import sys
input = sys.stdin.readline

ipv6 = input().strip()
shorten = ipv6.split(":")
full = []

if len(shorten) == 8:
    for i in range(8):
        full.insert(i, shorten[i])

        if len(full[i]) != 4:
            for j in range(4 - len(full[i])):
                full[i] = '0' + full[i]

    print(*full, sep=":")

else:
    half = ipv6.split("::")
    half1 = []
    half2 = []

    if len(half[0]) >= len(half[1]):
        half1 = half[0].split(':')

        for _ in range(7 - len(half1)):
            half2.append('')
        half2.append(half[1])

        full = half1 + half2

    elif len(half[0]) < len(half[1]):
        half2 = half[1].split(':')

        half1.append(half[0])
        for _ in range(7 - len(half2)):
            half1.append('')

        full = half1 + half2

    for i in range(8):
        if len(full[i]) != 4:
            for j in range(4 - len(full[i])):
                full[i] = '0' + full[i]
        else:
            continue

    print(*full, sep=":")
