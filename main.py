import telebot #pip install pyTelegramBotAPI
import configure #Token in another python file
from telebot import types

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(commands= ['get_info','info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да',callback_data='yes')
    item_no = types.InlineKeyboardButton(text='нет', callback_data='no')

    markup_inline.add(item_yes,item_no)
    client.send_message(message.chat.id,'Не желайте узнать больше информмации о вас',reply_markup=markup_inline)



@client.callback_query_handler(func= lambda call:True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True) #размер кнопки
        item_id = types.KeyboardButton('ID')
        item_nick = types.KeyboardButton('nickname')

        markup_reply.add(item_id,item_nick)
        client.send_message(call.message.chat.id,'Нажмите на одну из кнопок',reply_markup=markup_reply)

    elif call.data == 'no':
        pass


# @client.message_handler(content_types =  ['text'])
# def get_text(message):
#     if message.text.lower() == 'hello':
#         client.send_message(message.chat.id,'hello unknown user')
#     elif message.text.lower() == 'how are you':
#         client.send_message(message.chat.id,'I am okay,and you 😁')

@client.message_handler(content_types =  ['text'])
def get_text(message):
    if message.text == 'ID':
        client.send_message(message.chat.id,f'your Id is {message.from_user.id}')
    elif message.text.lower() == 'nickname':
        client.send_message(message.chat.id,f'your name is {message.from_user.first_name}  {message.from_user.last_name}')


client.polling(none_stop=True,interval=0)