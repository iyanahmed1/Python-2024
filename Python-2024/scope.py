""""def my_function():
    test=1# this is within the local scope of our function my_function
    print('This is my function', test)

test=0#this is within the global scope
my_function()
print('Test for global function', test)

#LEGB= Local,Enclosing,Global,Built-in

#if a variable is assigned inside a def, it is local to that function
#if a variable is assigned to an enclosing def, it is a nonclocal to the nested function
# if a variable is assigned outside of all the defs, it is global to the current file(module)

x=99
def function1():
    x=88"""""


"""""def outer():
    test=1#outer scope
    def inner():
        test=2#inner scope
        print('inner', test)

    inner()
    print('outer',test)

test=0
outer()
print('global', test)"""""

#global and nonlocal statement
def outer():
    test=1
    def inner():
        global test
        test=2#nearest enclosing statement(outer in this case)
        print('inner', test)

    inner()
    print('outer', test)
test=0
outer()
print('global',test)

"""""def lib():
    #outer scope
    lib_name="Ahmed's Library"
    #create a sections for books eg action
    def section():
        #enclosing scope
        section_name='action'
        def book():
            #local scope
            book_title='Maze Runner'
            print(f'Book_Title:{book_title}')
            print(f'Section_name:{section_name}')
            print(f'library:{lib_name}')
        book()
    section()
lib()"""""
