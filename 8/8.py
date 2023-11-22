import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

data = list(map(int, [i.strip() for i in open('data.txt', 'r').readlines()]))
settings = list(map(float, [i.strip() for i in open('settings.txt', 'r').readlines()]))

data = [i / 256 * 3.3 for i in data]
index_max = data.index(max(data))

data1 = np.array(data[:index_max])
data2 = np.array(data[index_max:])

t = np.linspace(0, 10, len(data))
max_t = t[index_max]

t1 = np.linspace(0, max_t, len(data1))
t2 = np.linspace(max_t, 10, len(data2))
data1_fix = np.polyval(np.polyfit(t1, data1, 15), t1)
data2_fix = np.polyval(np.polyfit(t2, data2, 12), t2)

data1_scat = [data1[i] for i in range(len(data1)) if i % 30 == 0]
data2_scat = [data2[i] for i in range(len(data2)) if i % 30 == 0]
t1_scat = [t1[i] for i in range(len(t1)) if i % 30 == 0]
t2_scat = [t2[i] for i in range(len(t2)) if i % 30 == 0]

fig = plt.figure()
ax = fig.gca()

# ax.set_xticks(np.arange(0, 10, 50))
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.5, linestyle='--')
ax.minorticks_on()
plt.xlim([0, 10.2])
plt.ylim([0, data2.max() + 0.1])

plt.scatter(t1_scat, data1_scat, color='black', s=np.array([0.7])*len(t1_scat))
plt.scatter(t2_scat, data2_scat, color='black', s=np.array([0.7])*len(t2_scat))
# plt.grid()
line1 = plt.plot(t1, data1_fix, color='blue', linewidth=1)
plt.plot(t2, data2_fix, color='blue', linewidth=1)

blue_line = mlines.Line2D([], [], color="blue", marker=".", markersize=10, label='V(t)')
ax.legend(handles=[blue_line])
plt.title('Процесс заряда и разряда конденсатора в RC-цепочке')
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
x1, y1 = 6, 2.3
x2, y2 = 6, 1.7
ax.text(x1, y1, 'Время заряда = ' + str(round(max_t, 2)) + ' с', style='italic',\
bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 1.5})
ax.text(x2, y2, 'Время разряда = ' + str(round(10 - max_t, 2)) + ' с', style='italic',\
bbox={'facecolor': 'grey', 'alpha': 0.3, 'pad': 1.5})


# plt.plot(t1, data1, color="red")
# plt.plot(t2, data2, color="blue")
plt.savefig('graf.png')
plt.show()
