#for numbers in[0,1,2,3,4]:
#    print(numbers)

#for number in range(5):
#    print(number)

#using a start and stop value for our loop
#num=list(range[200,500,2])
#print(num)

#print values between 101 and 115
#x=list(range(101,115,2))
#print(x)

#iterate over the following string'Hello'
#x='hello'
#for i in x:
#    print(i)

#exit a loop using break statement
#list=[10,20,30,40,50,60]
#for x in list:
#  print(x)
#   if x==50:
#      break

# create a list of grovceries containting cabbages, carrots, tomato, potatoes, onions, okra, mango, oranges 
#break loop at okra
#list=['cabbages','carrots','tomato','potatoes','onions','okra','mango','oranges']
#for x in list:
#    print(x)
#    if x=='okra':
#        break

#num1=[10,30,200,50,30,50,60]
#for x in num1:
#    if x >30:
#        continue
#    print(x)

# we have 3 lists people and their age and hometown, we want to print each personwith their ages
#people=['Hayyan','Branson','Eric']
#age=[21,24,25]
#hometown=['Tudor','Nyali','Mathira']
#use the for loop to find the length of our list using the len function
#print('Person','Age','hometown')
#for position in range(len(people)):
#    person=people[position]
#    ages=age[position]
#    town=hometown[position]
#    print(person,ages,town)
#the code above is not efficient, we use enumerate to make it more efficient 
#people=['Hayyan','Branson','Eric']
#age=[21,24,25]
#hometown=['Tudor','Nyali','Mathira']
#use the for loop to find the length of our list using the len function
#print('Person','Age','hometown')
#for position,person in enumerate(people):
#    ages=age[position]
#    town=hometown[position]
#    print(person,ages,town)

# the zip function to replace the positional indexing
people=['Hayyan','Branson','Eric']
age=[21,24,25]
hometown=['Tudor','Nyali','Mathira']
print('Person','Age','hometown')
for person,age,hometown,in zip(people,age,hometown):
    print(person,age,hometown)

