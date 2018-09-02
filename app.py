# TODO: format dates
# TODO: https://core.telegram.org/bots/api/#replykeyboardmarkup
# TODO: use beautiful soup to automatically
import os

import telegram
import pendulum
import time
import dotenv

from telegram.ext import Updater
from telegram.ext import CommandHandler


dotenv.load_dotenv(override=True)


TOKEN = os.getenv('BARCASBOT_TOKEN')
SAO_PAULO_TIME = pendulum.now('America/Sao_Paulo')
raw_schedules = ['06:00', '06:30', '07:00']
parsed_schedules = [
    (time.strptime(hour, '%H:%M').tm_hour, time.strptime(hour, '%H:%M').tm_min)
    for hour in raw_schedules
]


def get_praca_xv_schedule(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
    text=f'Praça XV (Rio) --> Araribóia (Niterói) {raw_schedules}')

def get_arariboia_schedule(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
    text=f'Araribóia (Niterói) --> Praça XV (Rio) {raw_schedules}')


bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

praca_xv_handler = CommandHandler('rj', get_praca_xv_schedule)
arariboia_handler = CommandHandler('nit', get_arariboia_schedule)

dispatcher.add_handler(praca_xv_handler)
dispatcher.add_handler(arariboia_handler)

updater.start_polling()

