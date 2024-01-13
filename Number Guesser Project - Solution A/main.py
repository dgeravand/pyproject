import random


def validate_input (user_guess):
    if not user_guess.isdigit():
        print('Invalid input, please try agian. ')
        return False
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print ("your guess is out of range. please try agian. your guess shoud be between 1 and 100 ")
        return False
    
    return True


def main():
    rand_num = random.randint(0,100)
    score = 100
    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        if user_guess == 'q':
            print('Thank you for playing. goodbye!')
            break
        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num > user_guess:
            print('your guess is too low, please try again: ')
            score -=1
        elif rand_num < user_guess:
            print('your guess is too high, please try again: ')
            score -=1
        else: 
            score = max(score,0)
            print(f'congratulations, your score is {score}, you guessed the correct number')
            break

if __name__ == '__main__':
    main()

