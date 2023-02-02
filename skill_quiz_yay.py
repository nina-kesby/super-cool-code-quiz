import random
import json

print("Skill values quiz!")

# return 1 = correct, 0 = wrong
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
        return 0
    else:
        print("good job first try")
        return 1
    


#names_list = ["back layout", "back tuck full", "back lay full", "1.5 twist", "double twist", "2.5 twist", "triple twist", "3.5 twist", "double tuck", "double pike", "tucked full in", "piked full in", "double twisting double tuck (Silivas)", "triple twisting double tuck (Biles II)", "double layout", "double layout half out (Biles I)", "full twisting double layout", "double twisting double layout (Moors)", "whip", "whip half twist", "whip full twist"]

#values_list = ["A", "B", "B", "C", "C", "D", "E", "F", "D", "D", "E", "E", "H", "J", "F", "G", "H", "I", "A", "B", "C"]


# trying to dictionary - ise the cute json file
all_skills_json = open('allSkills.json')
# returns JSON object as 
# a dictionary
skills_dict = json.load(all_skills_json)

# dictionary time



skill_names = list(skills_dict.keys())

score = 0
num_qs = 10
for i in range(num_qs):
    random_skill_num = random.randint(0, len(skill_names))
    current_skill = skill_names[random_skill_num]
    correct = skill_quiz(current_skill, skills_dict[current_skill])
    score += correct

print(f"congrats on finishing the quiz! Your score was {score}/{num_qs}. Yay gymnastics!")
