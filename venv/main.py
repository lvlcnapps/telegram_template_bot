from telebot import TeleBot
from telebot import formatting
from telebot import types
import usercleaning as uc
import genbuttons as gb


bot = TeleBot('')
users = {}

class MyBot():
    def __init__(self):
        print("Started")
        self.wait_for_data = 0


    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')

    @bot.message_handler(commands=['console'])
    def console(message):
        print("lol")

    @bot.message_handler(commands=['init'])
    def initUC(message):
        if (users.get(message.chat.id, -1) != -1):
            bot.send_message(message.chat.id, f'🚫Ошибка! У пользователя номер {message.chat.id} уже есть рабочее пространство',
                             parse_mode='html')
        else:
            temp_uc = uc.UserCleaning()
            users[message.chat.id] = temp_uc
            bot.send_message(message.chat.id, f'✅Создано рабочее пространство для пользователя номер {message.chat.id}', parse_mode='html')

    @bot.message_handler(commands=['delete'])
    def deleteUC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Ошибка! У пользователя номер {message.chat.id} еще нет рабочего пространства',
                             parse_mode='html')
        else:
            bot.wait_for_data = 5
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            bttn = types.KeyboardButton(text='Да')
            bttn2 = types.KeyboardButton(text='Нет')
            markup.add(bttn, bttn2)
            bot.send_message(message.chat.id,
                             f'⏳Подтвердите удаление, нажмите на кнопку "Да" внизу',
                             parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['progress'])
    def getProgressUC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id, f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.send_message(message.chat.id,
                             f'Список всех задач пользователя {message.chat.id}:\n{users.get(message.chat.id).getProgress()}',
                             parse_mode='html')

    @bot.message_handler(commands=['done'])
    def getProgressUC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.send_message(message.chat.id,
                             f'Список всех помеченных задач пользователя {message.chat.id}:\n{users.get(message.chat.id).getDone()}',
                             parse_mode='html')

    @bot.message_handler(commands=['make'])
    def makeDC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.wait_for_data = 1
            bot.send_message(message.chat.id,
                             f'Введите название задачи:',
                             parse_mode='html')

    @bot.message_handler(commands=['remove'])
    def removeDC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.wait_for_data = 2
            bot.send_message(message.chat.id,
                             f'Введите номер задачи:',
                             parse_mode='html')

    @bot.message_handler(commands=['removeDone'])
    def getProgressUC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            users.get(message.chat.id).removeDoneTasks()
            bot.send_message(message.chat.id,
                             f'Удалены все помеченные задачи',
                             parse_mode='html')

    @bot.message_handler(commands=['clear'])
    def clearUC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.wait_for_data = 6
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            bttn = types.KeyboardButton(text='Да')
            bttn2 = types.KeyboardButton(text='Нет')
            markup.add(bttn, bttn2)
            bot.send_message(message.chat.id,
                             f'⏳Подтвердите очистку задач, нажмите на кнопку "Да" внизу',
                             parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['mark'])
    def markDC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.wait_for_data = 3
            bot.send_message(message.chat.id,
                             f'Введите номер задачи:',
                             parse_mode='html')

    @bot.message_handler(commands=['unmark'])
    def unmarkDC(message):
        if (users.get(message.chat.id, -1) == -1):
            bot.send_message(message.chat.id,
                             f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                             parse_mode='html')
        else:
            bot.wait_for_data = 4
            bot.send_message(message.chat.id,
                             f'Введите номер задачи:',
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
        # MAKEDC
        if (bot.wait_for_data == 1):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                users.get(message.chat.id).makeTask(message.text)
                bot.send_message(message.chat.id,
                                 f'✅Создана задача {message.text} под номером {users.get(message.chat.id).getLastTask()} для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            bot.wait_for_data = 0
        # REMOVEDC
        if (bot.wait_for_data == 2):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                del_name = users.get(message.chat.id).removeTask(int(message.text))
                bot.send_message(message.chat.id,
                                 f'✅Удалена задача {del_name} для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            bot.wait_for_data = 0
        # MARKDC
        if (bot.wait_for_data == 3):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                temp_name = users.get(message.chat.id).markTask(int(message.text))
                bot.send_message(message.chat.id,
                                 f'✅Отмечена задача {temp_name} под номером {message.text} для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            bot.wait_for_data = 0
        # UNMARKDC
        if (bot.wait_for_data == 4):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                temp_name = users.get(message.chat.id).unmarkTask(int(message.text))
                bot.send_message(message.chat.id,
                                 f'✅Убрана метка с задачи {temp_name} под номером {message.text} для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            bot.wait_for_data = 0
        # CONFIRM DELETE UC
        if (bot.wait_for_data == 5):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                if (message.text == "Да"):
                    users.pop(message.chat.id)
                    gen = gb.GenButtons()
                    markup = gen.generate()
                    bot.send_message(message.chat.id, f'✅Удалено рабочее пространство для пользователя номер {message.chat.id}', parse_mode='html', reply_markup=markup)
                else:
                    gen = gb.GenButtons()
                    markup = gen.generate()
                    bot.send_message(message.chat.id,
                                     "🚫Отмена операции",
                                     reply_markup=markup)
            bot.wait_for_data = 0
        if (bot.wait_for_data == 6):
            if (users.get(message.chat.id, -1) == -1):
                bot.send_message(message.chat.id,
                                 f'🚫Не найдено рабочее пространство для пользователя номер {message.chat.id}',
                                 parse_mode='html')
            else:
                if (message.text == "Да"):
                    users.get(message.chat.id).clearTasks()
                    gen = gb.GenButtons()
                    markup = gen.generate()
                    bot.send_message(message.chat.id, f'✅Очищены все задачи пользователя номер {message.chat.id}', parse_mode='html', reply_markup=markup)
                else:
                    gen = gb.GenButtons()
                    markup = gen.generate()
                    bot.send_message(message.chat.id,
                                     "🚫Отмена операции",
                                     reply_markup=markup)
            bot.wait_for_data = 0
			
objBot = MyBot()

timer = 100
check = 0
while True:
    if timer == 1 or check == 0:
        try:
            bot.polling(none_stop=True, skip_pending=True)
        except BaseException:
            check = 1
    timer -= 1
    if timer <= 1:
        timer = 100
        check = 0