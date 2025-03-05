# Задача 1 Какой месяц
# month=1
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
locale.setlocale(locale.LC_ALL, 'rus')

month = 1

month_name = calendar.month_name[month]
print(f"Месяц под номером {month} — это {month_name}.")

# Задача 2 Наибольший общий делитель
import math

a = 600
b = 1012
print(math.gcd(a, b))

###### самостоятельная реализация 
def gcd(a: int, b: int) -> int:
    while b != 0:  
        a, b = b, a % b  
    return a  

a = int(input())
b = int(input())
result = gcd(a, b)
print(result)

# Задача 3 Проверка расширения файла
file = input()
extensions = ('png', 'jpg', 'jpeg', 'gif', 'svg')  # Используем кортеж вместо списка

if file.lower().endswith(extensions):
    print(f"Файл '{file}' имеет допустимое расширение.")
else:
    print(f"Файл '{file}' имеет недопустимое расширение.")

# Задача 4 Вискосный Год
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные;
# остальные годы, номер которых кратен 4, — високосные.
year = 2022

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("YES")
else:
    print("NO")