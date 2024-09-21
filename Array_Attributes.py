import numpy as np

#1. Shape Attribute
#displays the shape
''''a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a)
#change the shape'''
'''a.shape = (3,2) #change it to 3*2 matrix
print(a)'''

#2.reshape()
#to resize the existing array and storing the result in a new array object
'''a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)'''

#3. ndim
#display dimensions of the array object
a= np.arange(24)
'''print(a)
print(np.ndim(a))'''
#change the dimensions of a
b = a.reshape(6,4)
print(b)
print('dimension of a is : ', np.ndim(a))
print('dimension of b is : ',np.ndim(b))
c = a.reshape(3,4,2)
print(c)
print('dimension of c is: ',np.ndim(c))
print('shape of c is ',np.shape(c))