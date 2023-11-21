from  aiogram.types import KeyboardButton , ReplyKeyboardMarkup

def xizmatlar_button():
    n1 =  KeyboardButton(text="🔧 XIZLATLAR")
    n2 = KeyboardButton(text="📞 TELEFON ")
    n3 = KeyboardButton(text="🗓 ISH JADVALI")

    design = [
        [n1 , n2],
        [n3]
    ]

    tkm = ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True, one_time_keyboard=True)
    return tkm