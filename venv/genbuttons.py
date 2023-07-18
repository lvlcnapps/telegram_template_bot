from telebot import types

class GenButtons():
    def __init__(self):
        print('gen module created')

    def generate(self):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bttn = types.KeyboardButton(text='/init')
        bttn2 = types.KeyboardButton(text='/delete')

        bttn3 = types.KeyboardButton(text='/progress')
        bttn4 = types.KeyboardButton(text='/done')

        bttn5 = types.KeyboardButton(text='/make')
        bttn6 = types.KeyboardButton(text='/remove')

        bttn7 = types.KeyboardButton(text='/mark')
        bttn8 = types.KeyboardButton(text='/unmark')

        bttn9 = types.KeyboardButton(text='/clear')

        bttn10 = types.KeyboardButton(text='/help')

        markup.row(bttn, bttn2)
        markup.add(bttn10)
        markup.row(bttn3, bttn4)
        markup.row(bttn6, bttn5, bttn9)
        markup.row(bttn7, bttn8)
        #markup.add(bttn9)
        return markup