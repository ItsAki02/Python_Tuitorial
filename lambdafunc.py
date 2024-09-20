#wap for sorting words in a sentence from longest to shortest. if two words have same length, then display them in descending order of alphabets.
'''example: txt = 'Ram and Seeta wen to forest with Lakshman
expected output:Lakshman,forest,Seeta,with,went,and,Ram,to'''

s=input('Enter a text: ')
ls=[(word,len(word)) for word in s.split()]
print('Elements in the text with their lengths: ')
ls.sort(key = lambda x: (x[1],x[0]), reverse = True)
print('sorted elements:', ls)
ls1=[p[0] for p in ls]
print('sorted word:', ls1)