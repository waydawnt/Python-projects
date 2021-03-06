from telegram.ext import *
from telegram import *
import logging

TOKEN = 1234567890 //add your token code

updater = Updater(token = 'TOKEN', use_context= True)

dispatcher = updater.dispatcher

def start(update, context) :
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Sup, how u doing?")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def echo(update, context) :
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context) :
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id = update.effective_chat.id, text = text_caps)
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

def inline_caps(update, context) :
    query = update.inline_query.query
    if not query :
        return
    results = list()
    results.append(InlineQueryResultArticle (id = query.upper(), title='Capital', input_message_content = InputTextMessageContent(query.upper())))
    context.bot.answer_inline_query(update.inline_query.id, results)
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
