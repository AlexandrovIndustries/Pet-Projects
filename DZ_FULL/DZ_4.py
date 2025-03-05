
#1
def my_sqrt(x: float, n: float = 2) -> float:
    if n == 0:
        raise ValueError("Степень корня (n) не может быть равна нулю.")
    if x < 0 and n % 2 == 0:
        raise ValueError("Нельзя извлечь четный корень из отрицательного числа.")
    return x ** (1 / n)
number = 16
sqrt_result = my_sqrt(number)
print(f"Квадратный корень из {number} равен {sqrt_result}.")

cube_root_result = my_sqrt(number, 3)
print(f"Кубический корень из {number} равен {cube_root_result}.")


#2
def foo(filename: str, valid_extensions: list) -> bool:
    return any(filename.lower().endswith(f".{ext}") for ext in valid_extensions)

# Пример использования
file = 'Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

if foo(file, extensions):
    print(f"Файл '{file}' имеет допустимое расширение.")
else:
    print(f"Файл '{file}' имеет недопустимое расширение.")
    
#3
# Слейте воедино три словаря

def merge_dicts(*dicts):
 
    return {**dicts[0], **dicts[1], **dicts[2]}

dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}

merged_dict = merge_dicts(dict_a, dict_b, dict_c)
print(merged_dict)

#4
def sum_digits(number: int) -> int:
    return sum(int(digit) for digit in str(number))

number = int(input())
result = sum_digits(number)
print(f"Сумма цифр числа {number} равна {result}.")


#5 Уникальные числа
def all_unique(listing):
    return len(listing) == len(set(listing))

str_value = input()
listing = list(str_value)


print(all_unique(listing))  

numbers = [1, 4, 5]

print(all_unique(numbers))  

# 6.1

def print_list(my_list):
    for i, value in enumerate(my_list):
        print(f"НОМЕР {i} --> {value}")

print_list(["я", "не", "в", "отпуск", "я", "не", "в", "отпуск"])

# 6.2

def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f"КЛЮЧ <<{key}>> --> {value}")

print_dict({"key1": 2, "key3": False, "Приветствие": "Hello"})

#6.3

def print_list(my_list):
    for i, value in enumerate(my_list):
        print(f"НОМЕР {i} --> {value}")


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f"КЛЮЧ <<{key}>> --> {value}")


def print_overlord(mydict):
    for key, value in mydict.items(): 
        print(f"Анализируем ключ: {key}")  
        if isinstance(value, list): 
            print("Найден список:")
            print_list(value) 
        elif isinstance(value, dict): 
            print("Найден словарь:")
            print_dict(value)
        else:  
            print("Значение:", value)  
        print()  


print_overlord({
    "key1": 1,
    "key2": [1, 2, 3, 4], 
    "key3": "Hello", 
    "key4": {"ciao": "Mondo", "Привет": "О дивный мир"}
})

#******

def word_count(phrase):
  
    words = phrase.split()
    
    for word in words:
        print(word)
  
    print(f"Количество слов: {len(words)}")

word_count(input())

#* 2.0

def word_count(phrase):
    
    words = phrase.split()
    
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    total_words = len(words)

    for word, count in word_frequency.items():
        part = (count / total_words) * 100
        print(f"{word}: {part:.2f}%")

word_count(input())