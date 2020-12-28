from telebot import TeleBot
from telebot import types
import random
import pandas as pd 
import time


#random.randint(1,101)

#CAADAgADnSAAAulVBRiJ9erbmxeAFxYE - do slez
#CAADAgADqiAAAulVBRj4c2c1lQJVFBYE - vau
#CAADAgADnCAAAulVBRiFX8vuDxrGzxYE - ya sohranu tvoi sekret
#CAADAgADoiAAAulVBRioVRLFr_hpbxYE - v shoke



def predict1(message):
	i = random.randint(0,514)
	
	bot.send_message(message.chat.id, 'Погражаюсь в космос 🚀')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Звезды знают тебя')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Ммм, а ты не простой человек...')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Вижу 🔮')
	time.sleep(1)
	bot.send_message(message.chat.id, data.values[i][0])
	time.sleep(3)
	bot.send_sticker(message.chat.id, 'CAADAgADnSAAAulVBRiJ9erbmxeAFxYE')
	bot.send_message(message.chat.id, 'Давай еще предскажу?')
	

def predict2(message):
	i = random.randint(0,514)

	bot.send_message(message.chat.id, 'Я поведал много людей')
	time.sleep(2)
	bot.send_message(message.chat.id, 'А ты особенный человек')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Мой дым никогда не ошибается, и он знает твое будещее')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Вижу 🔮')
	time.sleep(1)
	bot.send_sticker(message.chat.id, 'CAADAgADqiAAAulVBRj4c2c1lQJVFBYE')
	time.sleep(2)
	bot.send_message(message.chat.id, data.values[i][0])
	time.sleep(3)
	bot.send_sticker(message.chat.id, 'CAADAgADnSAAAulVBRiJ9erbmxeAFxYE')
	bot.send_message(message.chat.id, 'Давай еще предскажу?')

def predict3(message):
	i = random.randint(0,514)

	bot.send_message(message.chat.id, 'Я не отсталый джин, пффф')
	time.sleep(1)
	bot.send_message(message.chat.id, 'У меня есть супер компьютер')
	time.sleep(2)
	
	bot.send_message(message.chat.id, 'Поищу-ка тебя в интернете')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Тааааак, чет не вижу')
	time.sleep(2)
	bot.send_sticker(message.chat.id, 'CAADAgADrSAAAulVBRisuTeYPsOfUBYE')
	bot.send_message(message.chat.id, 'Пфф, звезды лучше подскажут')
	
	bot.send_message(message.chat.id, 'Сим Салабим Ахалай Махайлай!!!!')
	time.sleep(3)
	
	bot.send_message(message.chat.id, 'Вижу 🔮')
	time.sleep(1)
	bot.send_message(message.chat.id, data.values[i][0])
	time.sleep(3)
	bot.send_sticker(message.chat.id, 'CAADAgADnCAAAulVBRiFX8vuDxrGzxYE')
	bot.send_message(message.chat.id, 'Твой секрет - мой секрет')

	bot.send_message(message.chat.id, 'Давай еще предскажу?')


def predict4(message):
	i = random.randint(0,514)

	bot.send_message(message.chat.id, 'Погражаюсь в космос 🚀')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Звезды знают тебя')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Звезды говорят что порой вам скучно и тоскливо')
	time.sleep(1)
	bot.send_message(message.chat.id, 'К стати вы видели мой фильм? Советую посмотреть в такие случаи')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Уил Смит красавчик. Люблю его 😍')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Сим Салабим Ахалай Махайлай!!!!')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Вижу 🔮')
	time.sleep(1)
	bot.send_message(message.chat.id, data.values[i][0])
	time.sleep(3)
	bot.send_sticker(message.chat.id, 'CAADAgADoiAAAulVBRioVRLFr_hpbxYE')
	bot.send_message(message.chat.id, 'Хотел бы я жить как человек в свободе, а не в лампе')
	time.sleep(2)
	bot.send_message(message.chat.id, 'Давай еще предскажу?')



data = pd.read_csv("fun.csv") 

bot = TeleBot('911036406:AAHifmAWjH_n07vFVaYaLZWPHZhNxt1RQA4')


@bot.message_handler(commands=['start'])
def start_message(message):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('Валяй')
	markup.row(itembtna)

	bot.send_sticker(message.chat.id, 'CAADAgADmCAAAulVBRhMhKHB9XZlHxYE')
	time.sleep(1)
	bot.send_message(message.chat.id, 'Давай раскрою тебе тайны грядущего')
	time.sleep(1)
	bot.send_message(message.chat.id, "Ну че начнем?", reply_markup=markup)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
	print(message)

@bot.message_handler(content_types=['text'])
def handle_sticker(message):
	if (message.text == 'Валяй'):
		r = random.randint(1,4)
		if (r == 1):
			predict1(message)
		if (r == 2):
			predict2(message)
		if (r == 3):
			predict3(message)
		if (r == 4):
			predict4(message)

		


bot.polling()