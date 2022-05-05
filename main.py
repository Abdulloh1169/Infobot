import m
from dataset.models import *

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
import logging
import helpers as h


def start(update: Update , context: CallbackContext):
    apliance = Device.objects.filter(parent = None, status=True)    
    keyboard_markup = h.build_keyboard(apliance)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to bot", reply_markup=keyboard_markup)



def handle_callback(update: Update, context: CallbackContext):
    return True


def message(update: Update, context: CallbackContext):
    mess = update.message.text
    if "Ortga" in mess and "Asosiy menyu" in mess:
        model = Device.objects.filter(parent = None, status=True) 
        keyboard_markup = h.build_keyboard(model)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Texnika turini tanlang", reply_markup=keyboard_markup)
        return True 

    elif "Ortga" in mess:
        name = mess[mess.index("(") + 1: mess.index(")")]
        model = Device.objects.get(name = name)
    else:
        model = Device.objects.get(name = update.message.text)
    

    # model = Device.objects.get(name = update.message.text)
    if(not model):
        return True
    elif(model.device_set.count() > 0):
        keyboard = h.build_keyboard(model.device_set.all())
        context.bot.send_message(text="Iltimos texnikalardan birini tanlang!", chat_id=update.effective_chat.id, reply_markup=keyboard)
    elif(model.getCharacteristics()):
        response = h.build_message(model)
        if response["message_type"] == "media":
            context.bot.send_media_group(chat_id=update.effective_chat.id, media=response["message"])
        elif response["message_type"] == "message":
            context.bot.send_message(chat_id=update.effective_chat.id, text=response["message"])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bu texnika turi bo'sh")

def catch_file(update: Update, context: CallbackContext):
    return True

def main():
    token = "5106147369:AAH0sIKOO1rlrawfk_FxMXkuEWnmKxZi7-o"
    updater = Updater(token)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(Filters.text & (~Filters.command), message)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()