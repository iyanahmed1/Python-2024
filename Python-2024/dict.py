
#order collection of items
#it stores elements in key/value pairs
#keys- uniques identifier associate with each other
capital_cities={'Kenya':'Nairobi','Uganda':'Kampala'}
print(capital_cities)


#retrive the capital cities
# we use the keys to retrive the values. we canot use the values to retrive keys
print(capital_cities['Kenya']) 
print(capital_cities['Uganda'])

#different ways of creating a dict
a=dict(Kenya='Nairobi', Uganda='Kampala')
b=dict(zip(['Kenya','Uganda'],['Nairobi','Kampala']))
c=dict([('Kenya','Nairobi'),('Uganda','Kampala')])
e=dict({'Kenya':'Nairobi','Uganda':'Kampala'})


