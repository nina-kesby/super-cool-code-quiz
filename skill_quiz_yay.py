print("Back tumbling skill values quiz!")

def skill_quiz (name, value):

    string_values = "ABCDEFGHIJK"

    
    lower_val, higher_val = string_values.split(value)

    loops = 1
    answer = input(f"What is the skill value of a {name}? ").upper()
    
    while answer != value:
        if answer in lower_val and answer:
            print("nah too low, it's way harder than that")
        elif answer in higher_val and answer:
            print ("no too high, it's not that hard jeez")
        else:
            print("THAT'S NOT A SKILL VALUE YOU NOOB BE BETTER")
        answer = input(f"what is the skill value of a {name}? ").upper()
        loops += 1
    print("yes good job! slayyyy")
    if loops > 1:
        print(f"lmao it took you {loops} guesses, go read the code more")
    else:
        print("wooo you got it first go, 10/10 slaying, FIG judge worthy")
    
#skill_quiz("back layout", "A")
#skill_quiz("triple double tuck (Biles II)", "J")
#skill_quiz("back tuck full", "B")
#skill_quiz("double tuck", "D")
#skill_quiz("back lay full", "B")
#skill_quiz("back 1.5 twist", "C")
#skill quiz("double twist", "C")

# omg wait is there a way to make it ask you a random one

names_list = ["back layout", "back tuck full", "back lay full", "1.5 twist", "double twist", "2.5 twist", "triple twist", "3.5 twist", "double tuck", "double pike", "tucked full in", "piked full in", "double twisting double tuck (Silivas)", "triple twisting double tuck (Biles II)", "double layout", "double layout half out (Biles I)", "full twisting double layout", "double twisting double layout (Moors)", "whip", "whip half twist", "whip full twist"]

values_list = ["A", "B", "B", "C", "C", "D", "E", "F", "D", "D", "E", "E", "H", "J", "F", "G", "H", "I", "A", "B", "C"]

# yay both lists have 21 things in them that's a good sign (positions 0 to 20)

# dictionary time

skills_dict = {"Moors": "I",
               "Silivas": "H"}

skill_names = list(skills_dict.keys())

import random

num_qs = 0
# ok let's try get it to ask more than one question
while num_qs in range(2):
    x = random.randint(0, 1)
    current_skill = skill_names[num_qs]
    skill_quiz(current_skill, skills_dict[current_skill])
    num_qs += 1

print("congrats on finishing the quiz! yay back tumbling")
    
    





