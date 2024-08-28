def sum_lists(numbers):
    Total=0
    for number in numbers:
        total +=number
        return Total
 

#write a function to write whether a number falls with a given range
def is_within_range(number,lower_bound,upper_bound):
    return upper_bound>=number>=lower_bound
print(is_within_range(1,3,5))

#write a function that accepts a string and counts the number of upper case and lower case leters
def count_numbers(string):
    upper_case=0
    lowercase=0
     
    for c in string:
        if c.isupper():
            count=+1
        if c.islower():
            count=-1



