import re
import json

skills_dic = {}

def skill_block_to_skills(skill_block, skills_dic, event):
    #print(f"Skill block: {skill_block}")
    reference = skill_block[0]
    skills = [""]*10
    for line in skill_block[1:]:
        line += " "
        skill_index = 0
        prev_letter = " "
        start_skill = True
        for i in range(len(line)):
            letter = line[i]
            if  prev_letter == " " and letter == " ":
                start_skill = True
                next
            
#            if 


            prev_letter = line[i]
            #if start_skill == True:
            if len(reference) > i + 1 and reference[i+1] == ".":
                skill_val = int(reference[i+2])
                if skill_val == 1 and reference[i+3] == "0" and reference[i+4] == "0": # checking Js
                    skill_val = 10
                #print(f"Skill val: {skill_val}")
                #print(skills)
                skills[skill_val - 1] = skills[skill_val - 1] + letter
                skill_index = skill_val-1
            else:
                if letter != "\n":
                    skills[skill_index] = skills[skill_index] + letter


            #    start_skill = False
    for i in range(len(skills)):
        skills[i] = skills[i].strip()
        skill = skills[i]
        if skill != "":
            skills[i] = f"({event}): {skill}"
            skills[i] = re.sub(" +", " ", skills[i]) 
            skills_dic[skills[i]] = chr(65 + i)

            


lines = []
vault = True
for line in open("2022code.txt"):
    if "Uneven Bars" in line:
        vault = False
    if not vault: # don't include vault in list of lines
        lines.append(line.replace("\n", ""))

skill_lines = []
event = 0
events = ["Vault", "Bars", "Beam", "Floor"]
for line in lines:
    if re.search(" *[(FX)(VT)(BB)(UB)] – Group", line) == None:
        if re.search("[0-9].000", line) == None:
            if re.search("A {10,50}B {10,50}", line) == None:
                skill_lines.append(line)



skill_block_lines = []
for line in skill_lines:
    if re.search(" — Elements", line) != None:
        event += 1
    else:
        if line != "":
            if re.search("[0-9]\.[0-9]{3}", line) != None:
                #print(skill_block_lines)
                if len(skill_block_lines) > 0: 
                    skill_block_to_skills(skill_block_lines, skills_dic, events[event])
                skill_block_lines = []
            skill_block_lines.append(line)
    

for skill in skills_dic:
    print(skill, skills_dic[skill])

json_skills = json.dumps(skills_dic)
with open("allSkills.json", "w") as outfile:
    outfile.write(json_skills)