text = 'hello python world, i am ready to python'
print(text.find('python')) #return index of first match string *case sensetive
print(text.rfind('python')) #return index of last match string *case sensetive
print(text.rfind('no')) #not fount -1 *case sensetive
print(text.rfind('python' , 30 , 60)) #return index of match string in rang *case sensetive
##
print(text.split()) #يفصل لي القائمة بان على المسافات
print(text.split(',')) #يفصل لي القائمة بان على ,
print(text.split('p', 1)) #يفصل لي القائمة بان على p و مره واحدة1 
##
print(' '.join(text.split(','))) #convert list to string and replace , -spilter- by ' '
##
value = 'A987'
print(value.isalnum()) #check if value all number & letter
print(value.isdigit()) #check if value all number only
##
textlong = '\n        python is back      '
print(textlong.strip()) #remove all sapeces & \n
print(textlong.lstrip()) #remove begening sapeces & \n
print(textlong.rstrip()) #remove end sapeces & \n
##
value1 = 'A\n9\n8\n7'
print(value1.replace('\n', '+')) #replace
print(value1.replace('\n', '+', 2)) #replace only first 2
##
textchange = 'Python Is BACK'
print(textchange.lower()) #change all text to lower
print(textchange.upper()) #change all text to upper
print(textchange.swapcase()) #change to other case
print(textchange.title()) #change first text to upper
##
fname = 'sondos'
lname = 'alrubaish'
major = 'ECE'
print('My name is {} {}, and i study {}'.format(fname, lname, major))
print('My name is {1} {2}, and i study {0}'.format(fname, lname, major))