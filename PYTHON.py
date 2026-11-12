import random

print("Welcome to the Number Guessing Game!")

print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")

secret_number = random.randint(1,100)

number=int(input("enter the number:"))

while (number!=secret_number): 

    if(number < secret_number):
        print("Votre réponse est trop basse. Réessayez!")
        
    else:
        print("Votre réponse est trop élevée. Réessayez!")
    number = int(input("Enter your guess: "))
    
print("Congratulations! You guessed the number:", secret_number)

    
    
