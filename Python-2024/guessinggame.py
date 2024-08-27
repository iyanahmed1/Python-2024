import random
targetno=random.randint(1,100)
guess=None
print('Welcome to the guessing game')
while guess!=targetno:
    try:
        guess=int(input('Please Enter your digit: ')) 
    if guess<targetno:
      print('Digit too low. Try again.')
    elif guess>targetno:
        print('Digit too high.Try again')
else:
    print('Congratualtions! You got it!')
