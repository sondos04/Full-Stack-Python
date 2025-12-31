age = [11, 15, 18, 20, 25, 30]

def filtered_ages(age):
    return age >= 18

print(list(filter(filtered_ages, age))) #filer by the condition in the function, and print in list format

def power_ages(age):
    return age ** 2

print(list(map(power_ages, age))) #powered by the condition in the function, and print in list format

age1 = [11, 15, 18, 20, 25, 30]

age1.sort() #يرتبها تصاعديا
print(age1)

age1.sort(reverse=True) #يرتبها تنازلي
print(age1)

age1.reverse() #يعكس ترتيبها من الاخير للاول
print(age1)

multilist = [num*2 for num in age1]
print(multilist) #يضرب كل عنصر ب 2

multilist = [num*2 for num in age1 if num > 20]
print(multilist) #يضرب كل عنصر ب 2