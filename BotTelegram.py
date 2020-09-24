#-- coding: utf-8 --
import requests 
import telebot
from telebot import types
import pymysql #biblioteca de conexao com o MySQL

conn = pymysql.connect(host='127.0.0.1', 
unix_socket='/opt/lampp/var/mysql/mysql.sock', #qual base ele deve se conectar
user='root', #usuario
passwd=None, #vazio
db='usuarios_telegram') #nome do banco de dados

# 127.0.0.1 é igual localhost

cur = conn.cursor() #conexao com o xampp


API_TOKEN = '1322517426:AAGMqNfE0XYkzpkKlxpz97D4azLgJrvmZbs' #@botfather

bot = telebot.TeleBot(API_TOKEN) #telebot-sumário e TeleBot(comando) aplicando token

user_dict = {} #variáveis únicas

class User: #minusculo
	def __init__(self,name):
		self.name = name
		self.age = None
		self.team = None
		self.mail = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.reply_to(message,"Tudo bem? Este é o bot que envia mensagens automaticas")#inserindo message
	cid = message.chat.id
	bot.send_message(cid,"Nosso id é: " + str(cid))
#	bot.register_next_step_handler(msg,process_name_step) #next

#def process_name_step(message):
#	try:
#		chat_id = message.chat.id
#		name = message.text
#		user = User(name)
#		user_dict[chat_id] = user #armazenando o chat_id desta conversa, único
#		msg = bot.reply_to(message,'Qual seu email?')
#		bot.register_next_step_handler(msg,process_mail_step)
#	except Exception as e:
#		bot.reply_to(message,e)

#def process_mail_step(message):
#	try:
#		chat_id = message.chat.id
#		mail = message.text
#		user = user_dict[chat_id]
#
		# nome da base
#		cur.execute("USE user_telegram") #executando base a ser usada
#		sql = "INSERT INTO usuario (nome_usuario,chat_id,email_usuario) VALUES (%s,%s,%s)" #comando
#		val = (user.name,str(chat_id),mail)
#		cur.execute(sql,val)#comando insert + valores
#		print(val) 
#		conn.commit() #ação do comando digitado
#		cur.close()
#		conn.close()
#		msg = bot.reply_to(message,'Obrigado por se cadastrar!')
		
#	except Exception as e:
#		bot.reply_to(message,e)

bot.enable_save_next_step_handlers(delay=2) #step
bot.load_next_step_handlers()

bot.polling()
