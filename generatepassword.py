import random
import string

def generator_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits=string.digits
    special = string.punctuation
    characcters=letters
    if numbers:
        characcters+= digits
    if special_characters:
        characcters += special

    pwd=""
    meet_criteria = False
    has_number=False
    has_special=False

    while not meet_criteria or len(pwd)<min_length:
        new_char=random.choice(characcters)
        pwd+= new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True

        meet_criteria=True
        if numbers:
            meet_criteria= has_number
        if special_characters:
            meet_criteria= meet_criteria and has_special

    return pwd    
 
min_length=int(input("enter the minimum length:"))
has_number= input("do you want to have numbers (y/n)?").lower()=="y"
has_special= input("do you want to have special character  (y/n)?").lower()=="y"
pwd = generator_password(min_length,has_number,has_special)
print("THE PASSWORD GENERATED IS :",pwd)


