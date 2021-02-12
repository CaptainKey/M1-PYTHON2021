import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,10,100)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('y = cos(x)')
plt.savefig('cos.png')
#plt.show()

img = plt.imread('cos.png')
plt.show()
print(img.shape)