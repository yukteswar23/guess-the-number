import random 
def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess!=random_number:
        guess = int(input(f'Guess a number btw 1 and {x} :'))
        print(guess)
        if guess<random_number:
            print("Sorry !  , guess again . Too Low")
        elif guess>random_number:
            print("Sorry , guess again . Too High ")
    print("YAY ! Bingo ")             

def computer_guess(x):
    low = 1 
    high = x 
    feedback = ''
    while feedback != 'c' :
        if low!= high: 
            guess = random.randint(low , high) 
        else :
            guess = low     
        feedback = input(f'is {guess} too high (H), too Low(L) or correct (c) ?? ')
        if feedback=='h':
            high = guess-1 
        elif feedback=='l':
            low = guess + 1 
    print("Yay ! your computer had guessed correctly ! ")

computer_guess(10)