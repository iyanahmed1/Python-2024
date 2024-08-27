#creating a function called shake()
#when creating a python program or system, whe have to put everything into file/modules 
#def shake():
#    print('This is a function')
#shake()

def my_func(name,location):#name and location are two arguements required by our program
    print(f'Hello {name}! Hope you are great. Tell me, are you from {location}')
#my_func('Mombasa','Hayyan')
#an arguements is a variable,value or object passed as a functionor method as input
#positional arguements are arguements that need to be included in the proper positional arguement
my_func(name='Hayyan',location='Mombasa')
#example above using a keyword arguement(*kwags*)
#a keyword arguement is an arguement that is passed to a function or method
#  which is proceded by a keyword and an equals sign(function(keyword=value))
#create a function to calculate the area of a triangle given the base and the height of the 10 qnd 15
# 2 arguements, base and height

def triangle_Area(base,height):
    area=0.5*base*height
    return area
#define triangle with the base of 10, height of 15
base=10
height=15
print(f'The area of the triangle is:{triangle_Area(base,height)}')

#0calaculate tip and total amount to be paid in the restaurant
def total_amount(bill_amount,tipPerc=10):#10 is the default value should there be no tip
    total_amount=bill_amount*(1+0.01*tipPerc)
    total_amount=round(total_amount,2)
    print(f'Please pay Ksh{total_amount}')

#write a python function to shoe employee()that
#a. should accept the employees name and salary and display both
#b if the salary is missing in the function call, then assign default value of 9000 to salary

def Employee(name,salary=9000):
    print('Name:',name,'Salary',salary)
Employee('Bronson',2000000)
Employee('Hayyan')

