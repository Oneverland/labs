import matplotlib.pyplot as plt

file = list(open('opendata.stat.txt'))[1:]

mas = [line.split(',') for line in file]

wiw = {}
for item in mas:
    if item[0] == 'Средняя пенсия' and item[1] == 'Забайкальский край' and item[2][:4] == '2018':
        wiw[item[2]] = item[3][:-1]
x = [g[5:7] for g in list(wiw.keys())]
y = [int(g) for g in list(wiw.values())]
print('средняя пенсия:', sum(y) / len(x))
plt.plot(x, y, 'b*-', markersize=10)
plt.xlabel('месяц')
plt.ylabel('значение')
plt.show()