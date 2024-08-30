#nested function
"""""def outer(x):
    def inner(y):
        return x+y
    return inner
five=outer(5)
result= five(6)
print(result)


#pass function as an arguement
def add(x,y):
    return x+y
def calculate(func,x,y):
    return func(x,y)
result=calculate(add,4,6)
print(result)

#return a function as a value
def greeting(name):
    def hello():
        return'hello,'+name+'!'
    return hello
greet=greeting('Atlantis')
print(greet())

#python decorator
def make_pretty(func):
    def inner():
        print('I got decorated')
        func()
    return inner
def ordinary():
  print('I am ordinary')

def make_pretty(func):
    #define the inner function
    def inner():
        #add some additional behaviour to decorated function
        print('I got decorated')
        #call original function
        func()
    #return the inner function
    return inner
#define ordinary function
def ordinary():
    print('I am ordinary')
#decorate ordinary function
decorated_func=make_pretty(ordinary)
#call the decorated function
decorated_func()"""""

#@ symbol with decorator
def make_pretty(func):
   def inner():
       print('I got decorated')
       func()
   return inner
@make_pretty
def ordinary():
    print('I am ordinary')
ordinary()

#decorating functions with parameters
def divide(a,b):
    return a/b
def smart_divide(func):
    def inner(a,b):
        print('I am going to divide',a, 'and', b)
        if b==0:
            print('Whoops! Cannot divide')
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(2,5)
divide(2,0)

#chaining decorators in python
def star(func):
    def inner(*args,**kwargs):
        print("%"*15)
        func(*args,**kwargs)
        print('*'*15)
    return inner
def percent(func):
    def inner(*args,**kwargs):
        print('%'*15)
        func(*args,**kwargs)
        print('%'*15)
    return inner
@star
@percent
def printer(msg):
    print(msg)
print('Hello')








































