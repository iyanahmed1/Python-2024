import random
target_no=random.randint(1,100)
print('Welcome to the guessing game!')
guess=None
while guess!= target_no:
        guess=int(input('User please enter your digit: '))
        if guess<target_no:
            print('Target too low. try again')
        elif guess>target_no:
            print('Target too hight.try again')
else:
     print('Congratulations! You guessed the correct number')
        


