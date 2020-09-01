import matplotlib.pyplot as plt
import numpy as np

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]

plt.plot(x1, y)
plt.show()

plt.plot(x1, y)
plt.xlabel('X1')
plt.ylabel('Y')
plt.title('Sample graph')
plt.show()

plt.plot(x1, y, marker='o', linestyle='--', color='r',label='tv')
plt.plot(x2, y, marker='*', linestyle='-', color='g', label='raddio')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Sample graph')
plt.legend(loc='lower right')
plt.show()

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')
 
plt.show()

data = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]
plt.boxplot(data)
plt.show()

import numpy as np
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

fig = plt.figure()
img1 = fig.add_subplot(121)
data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data, bins=10, normed=True)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
img2 = fig.add_subplot(122)
data = np.random.normal(2.0, 3.0, 1000)
plt.hist(data, bins=10, histtype='step')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

import matplotlib as mpl
plt.rcParams['font.size'] = 11.
plt.rcParams['font.family'] = 'Comic Sans MS'
plt.rcParams['axes.labelsize'] = 15.
plt.rcParams['xtick.labelsize'] = 10.
plt.rcParams['ytick.labelsize'] = 10.

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
plt.plot(x1,y, marker='s', linestyle='-', color='y',label='tv')
plt.plot(x2,y, marker='o', linestyle='--', color='g', label='raddio')
plt.xlabel('Advertisement Medium')
plt.ylabel('Sales')
plt.title('Advertisement effect on sales')
plt.legend(loc='lower right')
plt.show()
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
