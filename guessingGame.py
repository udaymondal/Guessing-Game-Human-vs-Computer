import random

def computerGuess(lowval, highval, randnum, count = 0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count

        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)

        else:
            count = count + 1
            return computerGuess(guess+1, highval, randnum, count)

    else:
        return -1
        # Number not found


#generate a random number

randnum = random.randint(1,101)

count = 0
guess = -99

while (guess!=randnum):
    # Get the user's guess
    guess = (int)(input("Guess a number between 1 and 100: "))

    if guess < randnum:
        print("higher your guess")
    elif guess < randnum:
        print("lower your guess")
    else:
        print("You guessed it!!!")
        break

    count = count + 1

print("You took " + str(count)+ " steps to guess the number")
print("Computer took" + str(computerGuess(0,100,randnum))+ " steps to complete")



