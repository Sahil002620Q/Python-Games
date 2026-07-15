import random
x = random.randint(1,10)
guess = int(input('make a guess : '))


def issmall(guess,x)
  if guess < x:
        print('small')
        guess = int(input('make another guess'))

while True:
    issmall(guess,x)

    elif guess > x:
        print('large')
        guess = int(input('make another guess'))

    elif guess == x:
        print('you guessed right')
        break
