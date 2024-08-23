#print output
#print accepts five parameters
#print(object=seperator=end=file=flush)

#flow control
#>=65-pass, <=65, fail
#break the normal flow of the operations
#flow control- the order in which the program should be executed
#desicion making
#conditional programming (branching) or looping
#conditional statement is if-else
# syntax
#if test expression
# statements(s)
#grade
#if(grade>=65
    #  'pass'
#else,
#'fail)

# assign grade 65>= pass 65>= fail
#grade=65
#if(grade>=65):
#    print('pass')
#else:
#   print('fail')

#arithmetic operators
# =, ==, <, /=, ,<>,
# 
# if we have more than one codition, we use the elif...else
# if(conditionA),
#   value if true
#   elif (if conditionA is false)
#   value if true
#else
#value if false

#Login checking system
##check username and password correctness

username=input('Enter Username:')
password=input('Enter Password:')
 
 #condition to check for username/pass
if username=='admin':
    if password=='1234':
        print('Loging Successful')
    elif password==12345:
        print('weak password')
    else:
         print('wrong password: plase check and correct')

#else:
#    if username=='guest':
   #     if password=='guest':
  #          print('login succesful')
 #       else:
#           print('incorrect username/inccorect password')

#create a new file for login validation using elif
# if the username filed is empty, return an error that the field cannnot be empty
# if the email doesnt contain an @ symbol, return invalid email
# if the password length is less than 8, notify user that password must be 8 characters
#otherwise register the user 




     
