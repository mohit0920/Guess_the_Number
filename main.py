from random  import  randint
randomNum = randint(1,100)
print('Hi! I am your Machine!')
print('I have a number in range of 1 to 100 \nYou Have to Guess it \n Lets See How much you know me. \nIf your guess is- \n  -within 10 of the number I will return "WARM" \n -further than 10 away from the number I will return "COLD!"\n Once you get closer 10 to my number than - \n If your next guess is - \n -closer to the number than the previous guess I will return "WARMER!" \n -farther from the number than the previous guess, I will return "COLDER!" ')
guessList = []
while True:
    guess = int(input('\nEnter your Guess'))
    if (guess < 1 ) or (guess > 100):
        print("Invailid guess.\n")
        pass
    else:
        guessList.append(guess)
    if guessList[-1] == randomNum:
        print(f'You Guess the number correctly number is {guessList[-1]} you have been guessed in {len(guessList)} Tries. \n')
        break
    elif guessList[-1] in range(randomNum - 10, randomNum +10):
        print('WARM!\n')
        break
    else:
        print('COLD!\n')
while True:
    guess = int(input('\nEnter your New Guess'))
    guessList.append(guess)
    if guessList[-1] == randomNum:
        print(f'\n \n You Guess the number correctly number is {guessList[-1]}. \nYou have guessed Me in  {len(guessList)} Tries. \n Our Understanding Percentage is - {100// len(guessList)}%\n\n Thank You.. For Playing With Me .. \n Regards \n Your Machine ')
        break
    elif abs(guessList[-1] - randomNum) < abs(guessList[-2] - randomNum):
        print('WARMER!\n')
    else:
        print('COLDER!\n')
