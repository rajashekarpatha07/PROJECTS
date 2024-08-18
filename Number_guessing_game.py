import random

computer_no = random.randint(0, 100)
score = 0

while True:
    userinput = int(input("guess a number: "))
    
    if userinput > computer_no:
        print("It's a lower number")
        score += 1
    elif userinput < computer_no:
        print("It's a higher number")
        score += 1
    else:  # userinput == computer_no
        print(f"You guessed correctly! The number is {computer_no}")
        score += 1
        break

print(f"You guessed it in {score} attempts!")
