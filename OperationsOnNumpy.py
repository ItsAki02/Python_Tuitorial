import numpy as np

#Element-wise Addition
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.arange(start=11,stop=20).reshape(3,3)
print(a)
print(b)

c = np.add(a,b)
print(c)

#element-wise multiplication
d = np.multiply(a,b)
print(d)

#element-wise subtarction
s = np.subtract(a,b)
print(s)

#element-wise division
z = np.divide(a,b)
print(z)

#element-wise Remainder
r =np.remainder(a,b)
print(r)

#matrix multiplication
t = np.matmul(a,b)
print(t)