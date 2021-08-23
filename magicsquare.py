s = []
for i in range(3):
    s.append([int(i) for i in input().split()])

general = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
suares = [general]
suares.append(general[::-1])
suares.append([i[::-1] for i in general])
suares.append(suares[2][::-1])
suares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
suares.append(suares[4][::-1])
suares.append([i[::-1] for i in suares[4]])
suares.append(suares[6][::-1])

min = 99
for i in suares:
    temp = 0
    for j in range(3):
        for k in range(3):
            temp += abs(s[j][k]-i[j][k])
    if temp < min:
        min = temp

print(min)