#Uses a variable to greet
#Author: Adrian Walshe

name = "Adrian"
print ("hello" + name ) 

#This wont work 
age = 34
#print ('your age is' + age)
print ('your age is' + str(age))
print ('Hello {} \tyour age is {}'.format(name,age))