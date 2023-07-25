from telebot import TeleBot
from telebot import formatting
from telebot import types
import usercleaning as uc
import genbuttons as gb
import os
import dbmod as db

f = open('token.txt', 'r')
bot = TeleBot(f.read())


class MyBot():
    def __init__(self):
        print("Started")
        self.wait_for_data = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands=['start643'])
def start(message):
    db.restore_table()
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands=['kill324'])
def kill(message):
    bot.send_message(message.chat.id, '<b>Пока</b>', parse_mode='html')
    os._exit(0)


@bot.message_handler(commands=['del278'])
def kill2(message):
    db.delete_all()
    bot.send_message(message.chat.id, '<b>Удалено</b>', parse_mode='html')


@bot.message_handler(commands=['console'])
def console():
    print("lol")


@bot.message_handler(commands=['progress'])
def getProgressUC(message):
    bot.send_message(message.chat.id, f'Список всех задач пользователя {message.chat.id}:\n{db.show_all()}',
                     parse_mode='html')


@bot.message_handler(commands=['done'])
def getProgressUC(message):
    bot.send_message(message.chat.id, f'Список всех задач пользователя {message.chat.id}:\n{db.show_marked()}',
                     parse_mode='html')


@bot.message_handler(commands=['make'])
def makeDC(message):
    bot.wait_for_data = 1
    bot.send_message(message.chat.id,
                     f'Введите имя задачи:',
                     parse_mode='html')


@bot.message_handler(commands=['remove'])
def removeDC(message):
    bot.wait_for_data = 2
    bot.send_message(message.chat.id,
                     f'Введите имя задачи:',
                     parse_mode='html')


@bot.message_handler(commands=['removeDone'])
def getProgressUC(message):
    db.clear_marked(message.chat.id)
    bot.send_message(message.chat.id,
                     f'Удалены все помеченные задачи',
                     parse_mode='html')


@bot.message_handler(commands=['clear'])
def clearUC(message):
    bot.wait_for_data = 5
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bttn = types.KeyboardButton(text='Да')
    bttn2 = types.KeyboardButton(text='Нет')
    markup.add(bttn, bttn2)
    bot.send_message(message.chat.id,
                     f'⏳Подтвердите очистку задач, нажмите на кнопку "Да" внизу',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['mark'])
def markDC(message):
    bot.wait_for_data = 3
    bot.send_message(message.chat.id,
                     f'Введите имя задачи:',
                     parse_mode='html')


@bot.message_handler(commands=['unmark'])
def unmarkDC(message):
    bot.wait_for_data = 4
    bot.send_message(message.chat.id,
                     f'Введите имя задачи:',
                     parse_mode='html')


@bot.message_handler(commands=['button'])
def button(message):
    gen = gb.GenButtons()
    markup = gen.generate()
    bot.send_message(message.chat.id,
                     "a",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def allHandlers_add(message):
    # MAKE DC
    if bot.wait_for_data == 1:
        kom = ["base_error5667"]
        try:
            kom = message.text.split()
            base = kom[1]
        except BaseException:
            base = "description"
        db.add_line(message.chat.id, kom[0], 0, base)
        gen = gb.GenButtons()
        markup = gen.generate()
        bot.send_message(message.chat.id,
                         f'Сделана задача {kom[0]} для пользователя номер {message.chat.id}',
                         reply_markup=markup)
        bot.wait_for_data = 0
    # REMOVE DC
    if bot.wait_for_data == 2:
        db.clear_task(message.chat.id, message.text)
        gen = gb.GenButtons()
        markup = gen.generate()
        bot.send_message(message.chat.id,
                         f'Очищена задача {message.text} для пользователя номер {message.chat.id}',
                         reply_markup=markup)
        bot.wait_for_data = 0
    # MARK DC
    if bot.wait_for_data == 3:
        db.update_line(message.chat.id, message.text, 1)
        gen = gb.GenButtons()
        markup = gen.generate()
        bot.send_message(message.chat.id,
                         f'Помечена задача {message.text} для пользователя номер {message.chat.id}',
                         reply_markup=markup)
        bot.wait_for_data = 0
    # UN MARK DC
    if bot.wait_for_data == 4:
        db.update_line(message.chat.id, message.text, 0)
        gen = gb.GenButtons()
        markup = gen.generate()
        bot.send_message(message.chat.id,
                         f'Убрана метка задачи {message.text} для пользователя номер {message.chat.id}',
                         reply_markup=markup)
        bot.wait_for_data = 0
    # CONFIRM CLEAR UC
    if bot.wait_for_data == 5:
        if message.text == "Да":
            db.clear_all(message.chat.id)
            gen = gb.GenButtons()
            markup = gen.generate()
            bot.send_message(message.chat.id, f'✅Очищены все задачи пользователя номер {message.chat.id}',
                             parse_mode='html', reply_markup=markup)
        else:
            gen = gb.GenButtons()
            markup = gen.generate()
            bot.send_message(message.chat.id,
                             "🚫Отмена операции",
                             reply_markup=markup)
        bot.wait_for_data = 0


"""
    @bot.message_handler(commands=['button_link'])
    def button_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    
"""
objBot = MyBot()

timer = 50
check = 0
while True:
    if timer == 1 or check == 0:
        try:
            bot.polling(none_stop=True, skip_pending=True)
        except BaseException:
            check = 1
    timer -= 1
    if timer <= 1:
        timer = 50
        check = 0
