# import telebot
# from telebot import types
#
# TOKEN = '6560118733:AAEYKRJBeuYhYU2iIJ49Uv64pcfC3I13Cp4'
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('service', 'schedule', 'contact')
#     bot.send_message(message.from_user.id, "Salom! Avtoserviz botiga xush kelibsiz!", reply_markup=user_markup)
#
# @bot.message_handler(commands=['service'])
# def handle_service(message):
#     service_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     service_markup.row('Xizmat 1', 'Xizmat 2')
#     service_markup.row('Orqaga')
#     bot.send_message(message.from_user.id, "Xizmatlardan birini tanlang:", reply_markup=service_markup)
#
# @bot.message_handler(func=lambda message: message.text == 'Xizmat 1' or message.text == 'Xizmat 2')
# def handle_selected_service(message):
#     selected_service = message.text
#     bot.send_message(message.from_user.id, f"Tanlangan xizmat: {selected_service}")
#
# @bot.message_handler(func=lambda message: message.text == 'Orqaga')
# def handle_back(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('service', 'schedule', 'contact')
#     bot.send_message(message.from_user.id, "Bosh sahifaga qaytish", reply_markup=user_markup)
#
# @bot.message_handler(commands=['schedule'])
# def handle_schedule(message):
#     message = ""
#     return message
#
# @bot.message_handler(commands=['contact'])
# def handle_contact(message):
#     message = "(90) 333 15 41 "
#     return message
# if __name__ == "__main__":
#     bot.polling(none_stop=True)







# import telebot
# from telebot import types
#
#
# TOKEN = '6560118733:AAEYKRJBeuYhYU2iIJ49Uv64pcfC3I13Cp4'
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('🔧🪛🔩 SERVICE', '📆 ISH JADVALI', '☎️TELEFON RAQAM')
#     bot.send_message(message.from_user.id, "Salom! Avtoserviz botiga xush kelibsiz!", reply_markup=user_markup)
#
# @bot.message_handler(commands=['🔧🪛🔩 SERVICE'])
# def handle_service(message):
#     service_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     service_markup.row('Xizmat 1', 'Xizmat 2')
#     service_markup.row('Orqaga')
#     bot.send_message(message.from_user.id, "Xizmatlardan birini tanlang:", reply_markup=service_markup)
#
# @bot.message_handler(func=lambda message: message.text == 'Xizmat 1' or message.text == 'Xizmat 2')
# def handle_selected_service(message):
#     selected_service = message.text
#     bot.send_message(message.from_user.id, f"Tanlangan xizmat: {selected_service} ")
#
# @bot.message_handler(func=lambda message: message.text == 'Orqaga')
# def handle_back(message):
#     user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     user_markup.row('🔧🪛🔩 SERVICE', '📆 ISH JADVALI', '☎️TELEFON RAQAM')
#     bot.send_message(message.from_user.id, "Bosh sahifaga qaytish", reply_markup=user_markup)
#
# @bot.message_handler(commands=['📆 ISH JADVALI'])
# def handle_jadval(message):
#      message = "kalotka"
#      return message
#
# @bot.message_handler(commands=['☎️TELEFON RAQAM'])
# def handle_contact(message):
#     message = "(90) 333 15 41 "
#     return message
#
#
#
# if __name__ == "__main__":
#      bot.polling(none_stop=True)



