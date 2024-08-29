def func(**kwargs):
    print(kwargs)

#all calls equivalent. they print out(a;1, B:42)
func(a=1, b=42)
func(**{'a':1,'b':42})
func(**dict(a=1, b=42))
#all the above return the same value
#adding** infront of the parameter name in the function deefinition tells python
#to use the name to collect a variable number of keyword parameters