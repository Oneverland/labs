def filtering(m):
    mas = []
    mas2 = []
    for i in m:
        if i == '\t':
            continue
        mas.append(i.strip().split(','))
    for i in mas:
        for j in i:
            mas2.append(j.strip().lower())
    return mas2[1:]


file = list(open('sport.txt', encoding='cp1251'))
not_filtered_sports = []


for item in file:
    k = 0
    temp = ''
    for i in item:
        if i == '\t':
            k += 1
        if k == 3:
            temp += i
        if k == 4:
            break
    not_filtered_sports.append(temp)

print(not_filtered_sports)
filtered_sports = filtering(not_filtered_sports)
print(filtered_sports)
print(len(filtered_sports))
print(file[-1])
sort_sports = sorted(set(filtered_sports))
c = 0
t = 0
print(sort_sports)
answ = {}
for sport in sort_sports:
    t += filtered_sports.count(sport)
    if filtered_sports.count(sport) in answ.keys():
        answ[filtered_sports.count(sport)].append(sport)
    else:
        answ[filtered_sports.count(sport)] = [sport]
q = 0
for i in sorted(answ.keys(), reverse=True):
    print(answ[i], i)
    q += 1
    if q == 3:
        break