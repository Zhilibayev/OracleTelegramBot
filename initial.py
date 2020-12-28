from telebot import TeleBot # Импортируем библеотеку который работает с Телеграм ботом
bot = telebot.TeleBot('903938685:AAH3UCqbLQi_wwWPpXPl7WIytSrCux18TUw') # Создаем переменную bot

@bot.message_handler(content_types=['text']) 	# Создаем функцию который будет реагировать на все типы сообщении
def start_message(message): 				
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start') # Реализуем отправку сообщения от самого бота

bot.polling() #Это линия кода должна стоять в конце. Он активирует сам Телеграм бот 