fruits=['Apple','Orange','Banana','Strawberry','Kiwi']
newfruits=['Grapes','Mango']
fruits.extend(newfruits)
fruits.remove('Strawberry')
print(len(fruits))

Persondetails={'Name':'Hayyan','Age':'20','City':'Mombasa'}
print(Persondetails)
Persondetails['occupation']= 'Business Woman'
Persondetails.update({'occupation':'Business Woman'})
print(Persondetails)
Persondetails.update({'Age':'21'})
print(Persondetails)

num1='123'
num1=int(num1)
print('data type',type(num1))
print(num1)

num2=124
num2=float(num2)
print('data type',type(num2))
print(num2)

num3=123.56
num3=str(num3)
print('data type',type(num3))
print(num3)

print(num1,num2,num3)