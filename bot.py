#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'твой токен бота'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура / кнопки
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")
	item3 = types.KeyboardButton("🦁 Мой Linkedin")
	item4 = types.KeyboardButton("🦊 Мои Чек листы")
	item5 = types.KeyboardButton("🪲 Мой баг репорт")
	item6 = types.KeyboardButton("🐝 Мои SQL запросы")
	item7 = types.KeyboardButton("🦄 Мой сайт")

	markup.add(item1, item2, item3, item4, item5, item6, item7)

	bot.send_message(message.chat.id, "Привет тебе от краба, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def interaction(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/tacitcoast')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/tacitcoast')
		elif message.text == '👤 Мой Linkedin':
			bot.send_message(message.chat.id, 'https://www.linkedin.com/in/anmalinovskaia')
		elif message.text == '🦊 Мои Чек листы':
			bot.send_message(message.chat.id, 'https://miro.com/app/board/uXjVPBkh9Mw=')
		elif message.text == '🪲 Мой баг репорт':
			bot.send_message(message.chat.id, 'https://docs.google.com/document/d/1NrNA62BaR3kO_Ko41JCIXnr6Ybj2oFodKCdN8qzFB6E/edit?usp=sharing')
		elif message.text == '🐝 Мои SQL запросы':
			bot.send_message(message.chat.id, 'https://docs.google.com/spreadsheets/d/1UwZicA_FdCaZ0VP5OzucteIedA_Z4xP_1i1l4nT_2hA/edit?usp=sharing')
		elif message.text == '🦄 Мой сайт':
			bot.send_message(message.chat.id, 'https://tacitcoast.github.io')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить 😢')

#оставляем бота всегда активным
bot.polling(none_stop=True)






#https://core.telegram.org/bots/api#available-methods
