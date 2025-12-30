alph = 'abcdefghijklmnopqrstuwxyz'
print(alph[0:10]) #finite rang
print(alph[:15]) #start from 0 to 15
print(alph[0:]) #start from 0 to the end
print(alph[0:5:2]) #start from 0 to 5, with length 2
print(alph[slice(0,5)]) #take only from 0 to 5
print(alph.index('jk')) #take only index for 'jk' *case sensetive
print(len(alph)) #length of the text
print(alph.count('s')) #counter *case sensetive
print('jk' in alph) #check *case sensetive (T/F)
print('sondos' not in alph) #check if not *case sensetive (T/F)
## merge and repete ##
fname = 'sondos'
lname = 'alrubaish'
print(fname +' '+ lname)
print((fname +' ') *3)