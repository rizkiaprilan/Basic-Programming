import os
import telebot as tb
from flask import Flask, request

TOKEN = '1127460118:AAGeXQZWA9yFTN1Sss6A52X5cYz2Vc1-xsw'
bot = tb.TeleBot(token=TOKEN) #authenticate

server = Flask(__name__) #buat server "__main__"

def sendmsg(message, text):
    bot.send_message(message.chat.id, text)

#bot side
@bot.message_handler(commands=['start'])
def startmsg(message):
    text = '''<b>Selamat datang pak rizki ada yang bisa bantu?</b>\nSilahkan ketik <b>Hello</b> dan dapatkan  balasan dari bot ini'''
    bot.send_message(message.chat.id,text,parser_mode='HTML')

@bot.message_handler(func=lambada,msg: msg.text is not None) #message bertipe string, bukan function
def reply_to_message(message):
    if 'Hello' in message.text.lower():
        sendmsg(message,'hai, {} semoga harimu menyenangkan'.format(message.from_user.first_name))

#server side
@server.route('/'+TOKEN,methods=['POST'])
def getMessage(): #pasang webhook
    bot.process_new_updates([tb.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return 'ok webhook sudah terpasang!',200

@server.route('/')
def webhook(): #menghapus webhook
    bot.remove_webhook()
    bot.set_webhook(url='https://bot-telegram-assistant.herokuapp.com/'+TOKEN)
    return 'ok webhook sudah terpasang!',200

if __name__=__main__:
    server.run(host="0.0.0.0",port=int(os.environ.get('PORT'),5000)) 

