import numpy as np
m,n = list(map(int, input('Enter the elements of array').split ()))
m1 = []
for i in range(m):
    ele = list(map(int, input('Enter the elements of array').split ()))
    m1.append(ele)
m1 = np.array(m1)    
print (m1.T)
print(m1.flatten())
