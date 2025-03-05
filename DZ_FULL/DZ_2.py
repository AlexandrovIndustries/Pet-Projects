# 1) Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
seconds = 10000
hour = seconds // 3600
minutes = (seconds - 3600 * hour) // 60
seconds_2 = seconds - (3600 * hour + minutes * 60)
print(f'{hour}:{minutes}:{seconds_2}')
#второй способ
total_seconds = 10000
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds_2_1 = remaining_seconds % 60
print(f'{hours}:{minutes}:{seconds_2_1}')


# 2) Напишите калькулятор который запрашивает на входе две переменные и знак, и в соответствии с знаком ( + - * / ) выводит результат

num1 = float(input("Введите первое число: "))
operator = input("Введите знак операции (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неверный знак операции!"


print(f"Результат: {result}")

# 3)Считайте 2 строки и выведите их на печать, разделив символом $.
# Попробуйте решить эту задачу как минимум 2 способами:

# с помощью конкатенации строк
# с помощью указания разделителя в параметре sep метода print

str1 = input()
str2 = input()

print(str1 + "$" + str2)

# Второй способ
str1 = input()
str2 = input()

print(str1, str2, sep="$")

# 4) Напишите поздравление с Днем рождения, где программа считает имя и возраст и выведет поздравление столько раз, сколько лет именнинику

name = input("Введите имя: ")
age = int(input("Введите возраст: "))

congratulation = f"С Днем рождения, {name}! Пусть исполняются все твои мечты!"

for _ in range(age):
    print(congratulation)