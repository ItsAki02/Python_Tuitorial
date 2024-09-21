import numpy as np

#converting a list into numpy array
#ls=[1,2,23]
#a=np.asarray(ls)   #by default the datatypes of the elements in the list are retained
#print(a,type(a))

'''a = np.asarray(ls,dtype=float)
print(a)'''

#tuple to numpy array
'''t = (1,2,3)
a = np.asarray(t)
print(a,type(a))'''

#list of tuples to array
ls = [(1,2,3),(4,5)]
a = np.asarray(ls)
print(a,type(a))
