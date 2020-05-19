from pathlib import Path
import re
import math

skillList = [
    "Admin",
    "Advocate",
    "Animals",
    "Art",
    "Astrogation",
    "Broker",
    "Carouse",
    "Deception",
    "Diplomat",
    "Drive",
    "Electronics",
    "Sensors",
    "Computers",
    "Remote Ops",
    "Sensors",
    "Engineer",
    "M-Drive",
    "E-Drive",
    "Life Support",
    "Power",
    "Explosives",
    "Flyer",
    "Gambler",
    "Gunner",
    "Gun Combat",
    "Energy",
    "Slug",
    "Heavy Weapon",
    "Investigate",
    "Jacob-of-All-Trades",
    "Language",
    "Leadership",
    "Mechanic",
    "Medic",
    "Melee",
    "Navigation",
    "Persuade",
    "Profession",
    "Science",
    "SeaFarer",
    "Steward",
    "Streetwise",
    "Survival",
    "Tactics",
    "Vacc Suit",
    "Custom 1",
    "Custom 2"]


templateFile = Path('SkillsTemplate.txt')
outputFile = Path('skills.txt')

template = ""
with templateFile.open() as f:
    template = f.read()

skillsCount = len(skillList)
orderedList = [""]*skillsCount

t1 = math.floor(len(orderedList[0::3]))
orderedList[0::3] = skillList[0:t1]

t2 = math.floor(len(orderedList[1::3]))
orderedList[1::3] = skillList[t1:t1+t2]

t3 = math.floor(len(orderedList[2::3]))
orderedList[2::3] = skillList[t1+t2:t1+t2+t3]

skills = ""
for s in orderedList:
    temp = re.sub("\{Name\}", s, template)
    temp = re.sub("\{name lower\}", s.lower(), temp)
    skills += temp


with outputFile.open("w") as f:
    f.write(skills)
