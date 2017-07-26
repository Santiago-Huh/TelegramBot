# -*- encoding: UTF8-*- #
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pymssql

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	update.message.reply_text('Bienvenido a BotSQl, ¿En que te puedo ayudar? '\
						'Para ver mis comandos usa:  /help')
def help(bot, update):
	update.message.reply_text('Estos son mis comandos:\n'\
					'Tablas 1: /tables\n'\
					'Tablas 2: /tables2\n')
def tables1(bot, update):
	server = ""
	user = ""
	password = ""
	base = ""
	conexion_sql = pymssql.connect(server, user, password, base)
	cur = conexion_sql.cursor()
	consulta = "SELECT TOP(10)  FROM "
	cur.execute(consulta)
	for row in cur.fetchall():
		resultado = row[0], row[1]
		update.message.reply_text(resultado)
def tables2(bot, update):
	server = ""
	user = ""
	password = ""
	base = ""
	conexion_sql = pymssql.connect(server, user, password, base)
	cur2 = conexion_sql.cursor()
	consulta2 = "SELECT CONVERT(nvarchar,) FROM "
	cur2.execute(consulta2)
	for row2 in cur2.fetchall():
		resultado2 = row2[0], row2[1], row2[2]
		update.message.reply_text(resultado2)

def echo(bot, update):
	update.message.reply_text(update.message.text)

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
	updater = Updater("TOKEN")

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("tables", tables1))
	dp.add_handler(CommandHandler("tables2", tables2))

	dp.add_handler(MessageHandler(Filters.text, echo))

	dp.add_error_handler(error)

	updater.start_polling()

	updater.idle()

if __name__=='__main__':
	main()
