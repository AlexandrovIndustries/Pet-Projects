#1
students = [
    ("Иванов О.", 4),
    ("Петров И.", 3),
    ("Дмитриев Н.", 2),
    ("Смирнова О.", 4),
    ("Керченских В.", 5),
    ("Котов Д.", 2),
    ("Бирюкова Н.", 1),
    ("Данилов П.", 3),
    ("Аранских В.", 5),
    ("Лемонов Ю.", 2),
    ("Олегова К.", 4)
]

def analyze_students(students):
 
    total_grades = sum(grade for _, grade in students)
    average_grade = total_grades / len(students)
    
    low_students = [name for name, grade in students if grade < average_grade]

    return average_grade, low_students

average_grade, low_students = analyze_students(students)
print(f"Средний балл: {average_grade:.2f}")
print("Отстающие ученики:", ", ".join(low_students))

########################################################################
#2 

def count_classes(filename):
    lec_count = 0
    pract_count = 0
    lab_count = 0
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            
            line = line.strip()
            
            if "лек" in line:
                lec_count += 1
            if "прак" in line:
                pract_count += 1
            if "лаб" in line:
                lab_count += 1
    
    return lec_count, pract_count, lab_count

filename = "DZ_5_txt.txt"

lec, pract, lab = count_classes(filename)
print('Лекций:', lec)
print('Практических:', pract)
print('Лабораторных:', lab)

########################################################################
#3 TELEGRAM
import requests

from config import TOKEN

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

params = {
    "chat_id": 72479****,  
    "text": "Привет, это мой бот!"
}

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# response = requests.get(url)
# print(response.json())

response = requests.post(url, params=params)
print(response.json()) 

####################################################################3
#4 Тетради 

import os

directory = r"D:\ПЕТСИКИ\DZ_5_FULL\Notebooks"

files = os.listdir(directory)

for file in files:
    full_path = os.path.join(directory, file)
    if os.path.isfile(full_path):
        print(file)
        
###################################################################

#5 

from collections import Counter

def analyze_text(text):
   
    words = [word.strip(".,!?—").lower() for word in text.split() if word.strip(".,!?—")] 

    if not words:
        return "", ""

    most_common_word = Counter(words).most_common(1)[0][0]

    longest_word = max(words, key=len)

    return most_common_word, longest_word


text = """
Варкалось. Хливкие шорьки Пырялись по наве, И хрюкотали зелюки, Как мюмзики в мове.

О, бойся Бармаглота, сын! Он так свирлеп и дик! А в глу́ше ры́мит исполин — Злопастный Брандашмыг!

Но взял он меч, и взял он щит, Высоких полон дум. В глущобу путь его лежит Под дерево Тумтум.

Он стал под дерево и ждёт. И вдруг граахнул гром — Летит ужасный Бармаглот И пылкает огнём!

Раз-два, раз-два! Горит трава, Взы-взы — стрижает меч, Ува! Ува! И голова Барабардает с плеч!

О светозарный мальчик мой! Ты победил в бою! О храброславленный герой, Хвалу тебе пою!

Варкалось. Хливкие шорьки Пырялись по наве. И хрюкотали зелюки, Как мюмзики в мове.
"""

most_common, longest = analyze_text(text)

print(f"Наиболее часто встречающееся слово: {most_common}")
print(f"Самое длинное слово: {longest}")