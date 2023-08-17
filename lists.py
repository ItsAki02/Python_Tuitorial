'''my_list = [1, 2, 3]
print(my_list)

fruits = ['Apple', 'lichi', 'grapes']
fruits[0] = 'Mango'

print(fruits)
#del fruits'''

'''num = [0, 1, 2, 3, 4, 5]

print(num)
print(num[2:5])
print(num[-1:0:-2])'''

#list comprehension

# a = [0, 1, 2 , 3, 4, 5, 6 , 7, 8, 9]

a = [x for x in range(100) if x % 2 == 0]
print(a)

b = [3**i for i in range(10)]
print(b)