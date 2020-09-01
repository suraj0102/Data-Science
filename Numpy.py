import numpy as np
a = np.array([1,2,3,4])
print(a.shape)
import numpy as np
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.shape)
print(b)
print(b[0]) 
print(b[0][0])  
print(b[1][0]) 
print(b[2][0]) 
print(b[2,0])

import numpy as np
b = np.zeros((3,3)) 
print(b)

import numpy as np
b = np.ones((3,3)) 
print(b)

import numpy as np
b = np.full((2,2), 8) 
print(b)

import numpy as np
b = np.eye(3) 
print(b)

import numpy as np
b = np.random.random((2,2)) 
print(b)

import numpy as np
b = np.arange(10) 
a = np.arange(1,11, dtype=float) 
print(a)
c = np.arange(2,3, 0.1)
print(c)

import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[0:2] 
print('b',b)
b = a[1:2] 
print('b',b)
b = a[0:1,0:4] 
print('b',b)
b = a[0:1,0:2] 
print('b',b)
b = a[0:1,2:4] 
print('b',b)

import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[1:2,0:4] 
print('b',b)
b = a[1:2,1:2] 
print('b',b)
b = a[:2,0:2] 
print('b',b)
b = a[:2,1:3] 
print('b',b)
b = a[1:3,2:4] 
print('b',b)

import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]])
print(a.shape)
b = a[[0,1,2],[0,1,0]] 
print(b)
print(b.shape)

import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = a[0:2,1:3] 
print(b)
b[0,0]=20 
print(b)
print(a)

import numpy as np
a = np.array([[1,2],[2,4]])
b = np.array([[7,8]])
c = np.concatenate((a,b), axis=0)
print(c)
d = np.concatenate((a,b.T), axis=1)
print(d)

import numpy as np
a = np.array([[1,2],[3,4]], dtype=np.int32)
b = np.array([[5,6],[7,8]], dtype=np.int32)
print(a+b)
print(np.add(a,b))
print(a-b)
print(np.subtract(a,b))
print(a*b)
print(np.multiply(a,b))
print(a/b)
print(np.divide(a,b))
print(np.sqrt(a))
print(a.dot(b))
print(np.dot(a,b))

a = np.array([[1,2],[3,4]], dtype=np.int32)
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
height = performance
width = 0.8
bottom = 0
plt.bar(y_pos, height, width, bottom, align='center', alpha=1.0)
plt.xticks(y_pos,objects)
plt.ylabel('Usage')
plt.xlabel('Languages')
plt.title('Programming language usage')
plt.show()

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4],'bs') # 'ro' for round  'g^' for triange and 'bs' for square. By default line
plt.ylabel('some numbers')
plt.show()

import matplotlib.pyplot as plt
plt.plot([1, 2, 8, 4],[4,2,6,7]) 
plt.ylabel('some numbers')
plt.show()

import matplotlib.pyplot as plt
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.plot(t, s, lw=3)
plt.show()

