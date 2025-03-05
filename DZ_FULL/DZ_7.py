#1 Site check 

# @checksitebot_bot

import requests
import telebot
from telebot import types

TOKEN = "7224984270:AAGFqyl6j6Dg_uiHxbu6Zkn6zLO3cEciH8A"

bot = telebot.TeleBot(TOKEN)

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return f"Сайт {url} доступен. Код ответа: {response.status_code}"
        else:
            return f"Сайт {url} недоступен. Код ответа: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Ошибка при проверке сайта {url}: {e}"

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Проверить сайт")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для проверки доступности сайтов. "
        "Отправь мне URL сайта, и я проверю его доступность.",
        reply_markup=markup,
    )

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(
        message.chat.id,
        "Просто отправь мне URL сайта (например, https://example.com), "
        "и я проверю его доступность.\n\n"
        "Используй команду /start, чтобы вернуться к началу.",
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip().lower()
    if text == "помощь":
        send_help(message)
    elif text == "проверить сайт":
        bot.send_message(message.chat.id, "Отправь мне URL сайта для проверки.")
    else:

        if not text.startswith(("http://", "https://")):
            text = "https://" + text
        result = check_website(text)
        bot.send_message(message.chat.id, result)


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)


# 2 Bot Text 
# @my_bot_token_bot

import telebot
from telebot import types
import re
from collections import Counter

TOKEN = "7300681305:AAEn4dzJeaTdMbEuaOUMnZa53kR4qCJo5dU"

bot = telebot.TeleBot(TOKEN)

STOP_WORDS = set([
    "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как", "а", "то", "все", "она", "так", "его", 
    "но", "да", "ты", "к", "у", "же", "вы", "за", "бы", "по", "только", "ее", "мне", "было", "вот", "от", 
    "меня", "еще", "нет", "о", "из", "ему", "теперь", "когда", "даже", "ну", "вдруг", "ли", "если", "уже", 
    "или", "ни", "быть", "был", "него", "до", "вас", "нибудь", "опять", "уж", "вам", "ведь", "там", "потом", 
    "себя", "ничего", "ей", "может", "они", "тут", "где", "есть", "надо", "ней", "для", "мы", "тебя", "их", 
    "чем", "была", "сам", "чтоб", "без", "будто", "чего", "раз", "тоже", "себе", "под", "будет", "ж", "тогда", 
    "кто", "этот", "того", "потому", "этого", "какой", "совсем", "ним", "здесь", "этом", "один", "почти", 
    "мой", "тем", "чтобы", "нее", "сейчас", "были", "куда", "зачем", "всех", "никогда", "можно", "при", 
    "наконец", "два", "об", "другой", "хоть", "после", "над", "больше", "тот", "через", "эти", "нас", "про", 
    "всего", "них", "какая", "много", "разве", "три", "эту", "моя", "впрочем", "хорошо", "свою", "этой", 
    "перед", "иногда", "лучше", "чуть", "том", "нельзя", "такой", "им", "более", "всегда", "конечно", "всю", 
    "между"
])

def analyze_text(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)

    unique_words = set(words)
    unique_word_count = len(unique_words)

    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_freq = Counter(filtered_words)
    most_common_words = word_freq.most_common(5) 

    return {
        "sentence_count": sentence_count,
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "most_common_words": most_common_words,
    }

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Анализировать текст")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для анализа текста. Отправь мне текст, и я предоставлю статистику: "
        "количество предложений, слов, уникальных слов и самые популярные слова.",
        reply_markup=markup,
    )

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(
        message.chat.id,
        "Просто отправь мне текст, и я проанализирую его. Вот что я могу:\n"
        "- Посчитать количество предложений.\n"
        "- Посчитать количество слов.\n"
        "- Посчитать количество уникальных слов.\n"
        "- Найти самые популярные слова (исключая союзы и предлоги).\n\n"
        "Используй команду /start, чтобы вернуться к началу.",
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip().lower()
    if text == "помощь":
        send_help(message)
    elif text == "анализировать текст":
        bot.send_message(message.chat.id, "Отправь мне текст для анализа.")
    else:
        analysis = analyze_text(message.text)
        response = (
            f"  Статистика текста:\n"
            f"- Количество предложений: {analysis['sentence_count']}\n"
            f"- Количество слов: {analysis['word_count']}\n"
            f"- Количество уникальных слов: {analysis['unique_word_count']}\n"
            f"- Самые популярные слова: {', '.join([f'{word} ({count})' for word, count in analysis['most_common_words']])}"
        )
        bot.send_message(message.chat.id, response)

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)

    
# # 3 Calculate bot 
# # @Calculate_bot_bot
    
import telebot
from telebot import types

TOKEN = "7724384289:AAHr5dtfPquihMZABLJnSohLQFI7FYG83Fw"

bot = telebot.TeleBot(TOKEN)

current_expression = ""

def create_calculator_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    
    row1 = ["7", "8", "9", "/"]
    row2 = ["4", "5", "6", "*"]
    row3 = ["1", "2", "3", "-"]
    row4 = ["0", ".", "C", "+"]
    row5 = ["="]
    
    markup.add(*row1)  
    markup.add(*row2)
    markup.add(*row3)  
    markup.add(*row4)
    markup.add(*row5)  
    return markup

@bot.message_handler(commands=["start"])
def send_welcome(message):
    global current_expression
    current_expression = ""  
    bot.send_message(
        message.chat.id,
        '''
        Привет! Я бот-калькулятор. Используй кнопки ниже для вычислений. 
        Ты можешь так же использовать кнопки на клавиатуре для корректного ввода выражения. 
        Отправь выражение, введеное с клавиатуры, чтобы проверить его корректность.
        Чтобы получить результат выражения - нажми на "=" в кнопках бота''',
        reply_markup=create_calculator_keyboard(),
    )

@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    global current_expression
    
    text = message.text.strip()
    
    if text == "C":
        current_expression = ""
        bot.send_message(
            message.chat.id,
            "Выражение очищено.",
            reply_markup=create_calculator_keyboard(),
        )
    elif text == "=":
        try:
            result = str(eval(current_expression))
            bot.send_message(
                message.chat.id,
                f"Результат: `{result}`",
                parse_mode="Markdown",
                reply_markup=create_calculator_keyboard(),
            )
            current_expression = result  
        except ZeroDivisionError:
            bot.send_message(
                message.chat.id,
                "Ошибка: деление на ноль.",
                reply_markup=create_calculator_keyboard(),
            )
            current_expression = ""
        except Exception as e:
            bot.send_message(
                message.chat.id,
                f"Ошибка: некорректное выражение.",
                reply_markup=create_calculator_keyboard(),
            )
            current_expression = ""
    else:
        current_expression += text
        bot.send_message(
            message.chat.id,
            f"Текущее выражение: `{current_expression}`",
            parse_mode="Markdown",
            reply_markup=create_calculator_keyboard(),
        )

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
