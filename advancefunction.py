#Positional Arguments: order is important
def info(name , age):
    print('hi my name is ' , name , 'and i am ' ,age, ' years old')
info('sondo' , '21')

#Keyword Arguments: order is not important because of keyword
def info(name , age):
    print('hi my name is ' , name , 'and i am ' ,age, ' years old')
info( age ='21' , name = 'sondo') #key word should be same word of argument 

#Default Parameter
def info(age ='21' , name = 'sondo'):
    print('hi my name is ' , name , 'and i am ' ,age, ' years old')
info('25') #replace the defualte by the positional argument

#Argument Packing: multi argus in one paramete as tuple
def aver(*num):
    print(num)
    total = sum(num)
    leng = len(num)
    averge = total / leng
    print(averge)
aver(2,3,4,5,6,7,8,0,9)

#Argument Unpacking: ungroup the list
def info(name1 , name2, name3 ):
    print('hi' , name1 , ',' ,name2, ' and', name3)

names = ['sondos' , 'lolo' , 'eva']
info(*names)

# Dictionary Packing: print both keyword and value
def info(**kwargs):
    print(kwargs)
    print('hi i am ',kwargs['name'])
info(name = 'sondos' , age = '21')

#Dictionary Unpacking
def info(name , age):
    print('hi i am ',name)

d = {'name':'sondos' , 'age':'21'}
info(**d)

def foo(*args):
    print(args)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
foo(*l1, *l2)