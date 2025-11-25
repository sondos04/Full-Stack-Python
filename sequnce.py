#list
names = ['Sondos', 21, 165.7, 'Lina'] #list can contain different data types
print(names)
print(type(names)) #list is a data type
print('First item in the list is: ', names[0]) #accessing list item by index start from 0
#change the value of an item in the list
names[3] = 'hello'
print(names)
#add item to the end of the list
names.append('Raghad')
print(names)
#add item to the list
names.insert(2, 'ECE') #insert(index, value)
print(names)
#remove item from the list
names.remove(165.7) #remove by value
print(names)
#remove all items from the list
names.clear()
print(names)

#--------------------
#tuple -the value unchangeable-
child_one = ('Sondos', 'ECE', 21)
child_two= 'Sondos', 'ECE', 21
print(child_one)
print(child_two)
print(type(child_one)) #tuple is a data type
print(child_one[0]) #accessing tuple item by index start from 0
#child_one[0] = 'Lina' #this will cause error because tuple value unchangeable

#--------------------
#dictionary -key:value-
me = {'name':'Sondos''rahaf', 'major':'ECE', 'age': 21}
print(type(me)) #dictionary is a data type
print(me)
print('My name is ', me['name']) #accessing dictionary value by key
print(me.values()) #get all values in the dictionary
print(me.keys())   #get all keys in the dictionary
me['age'] = 22     #change value by key
print(me)
me['height'] = 1.65 #add new key:value
print(me)
me.pop('major')     #remove key:value by key
print(me)
me.clear()         #remove all items in the dictionary
print(me)