# # create a script to output hello world
# print('hello world')
# # create a variable named name that stores my name
# fname = 'Hayyan'
# surname ='Mohamed'
# age = 20

# print(fname, surname,type (surname))
# print('my age is',age, type(age))


#  ask the user to input their names and age
# fname = input('please enter your first name:')
# suranme = input('please enter your surname:')
# age = input('please enter your age:')
# # get your user output
# print('Your First name is: ',fname)
# print('Your surname is: ',suranme)
# print('Your age is: ',age)


# print('Your full details:',fname , suranme ,age)
# num1 =5/6
# print(num1,'is of type', type(num1) )

# num2 = 2.0
# print(num2, 'is of type',type(num2))
# num3= 1+2j
# print(num3, 'is of type',type(num3))
# name= 'python'
# print(name,type(name))
# message='python for beginners'
# print(message,type(message))

language=['python','Java','javaScript','swift']
# print(language[3])
# language.insert(4,'C#')
# print(language[4])

language.append('C#')
print(language[4])
language.append('C+')
print(language[5])

new_languages= ['Go','SQL']
language.extend(new_languages)
print(language[6])
print(len(language))