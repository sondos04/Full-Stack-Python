# This is a simple print statement in Python.
print('Hello world!')
print('Welcome to Full-Stack Python.')

#creat variables
name = 'Sondos'     #string variable -you can use " "-
age = 21            #integeer variable -it could be - or + -
height = 1.65       #float variable -it could be - or + -
is_student = True   #boolean variable -True/False-
home_address = None #null variable -no value-
# name, age, height, is_student = 'Sondos', 21, 1.65, True

#for know the type of variable
print('type of varible name is ', type(name))

#take value from user
value_from_user = input('Enter your age: ')
print('you are ', value_from_user, 'years old!')

#change the formate of the output
float_age = float(age)   #21.0
int_height = int(height) #1
str_height = str(height) #1.65 -as str-