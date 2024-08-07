import telebot
from telebot import types

bot = telebot.TeleBot('7489836246:AAHUOmtuZYhSGs1YGweMXbKbTHfF3zjd1X8')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    bot.send_message(message.chat.id, "для того чтобы посмотреть список всех команд напиши /help")
    bot.send_message(message.chat.id, "для того чтобы посмотреть описание всех команд напиши /help1")


@bot.message_handler(commands=['help1'])
def start_message(message):
    bot.send_message(message.chat.id, "мой бот - даст вам ссылку на моего другого бота, которого я создал в 9 классе(2 года назад), в нём вы можете найти любой учебник и посмотреть его или скачать")
    bot.send_message(message.chat.id, "немного обо мне - немного информации обо мне, да, вот так банально)")
    bot.send_message(message.chat.id, "связь со мной - если вам понравился мой бот или хотите сотрудничать, обязательно пишите. Просто так лучше не писать, а то могу заблокировать")


@bot.message_handler(commands=['sozdatel'])
def start_message(message):
    bot.send_message(message.chat.id, "ссылка для моего создателя:) https://t.me/Wolan_d")


@bot.message_handler(commands=['help'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("мой бот")
    item2 = types.KeyboardButton("немного обо мне")
    item3 = types.KeyboardButton("связь со мной")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "мой бот":
        bot.send_message(message.chat.id, "https://t.me/Analit1k_bot")
    if message.text == "немного обо мне":
        bot.send_message(message.chat.id, "Кирилл, 17 лет, Учился у Вики с ноября и поступил в ИТМО) ")
    if message.text == "связь со мной":
        bot.send_message(message.chat.id, "https://t.me/Wolan_d")


bot.infinity_polling()