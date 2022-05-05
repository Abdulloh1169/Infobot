from telegram import (
    KeyboardButton, 
    ReplyKeyboardMarkup,
    InputMediaPhoto,
)


def build_keyboard(objects, resize_keyboard = True):
    keyboard = []
    for object in objects:
        keyboard.append([object.name])
    
    sample = objects[0]
    if(sample.parent != None and sample.parent.parent != None):
        keyboard.append([f"Ortga ({sample.parent.parent.name})"])
    elif(sample.parent != None):
        keyboard.append([f"Ortga (Asosiy menyu)"])

    return ReplyKeyboardMarkup(keyboard, resize_keyboard)


def build_message(object):
    message = object.getCharacteristics().body
    media = object.getMedia()

    """
    mediagroup = []
    f = open("media/1.jpg", "rb")
    l = open("media/2.jpg", "rb")
    mediagroup.append(InputMediaPhoto(media=f, caption=message))
    mediagroup.append(InputMediaPhoto(media=l))
    """
    
    if media:
        media_group, first = [], True
        for file in media:
            if first:
                media_group.append(InputMediaPhoto(media=open(str(file.mediafile), "rb"), caption=message))
            else:
                media_group.append(InputMediaPhoto(media=open(str(file.mediafile), "rb")))
            first = False
        return {"message": media_group, "message_type": "media"}
    else:
       return {"message": message, "message_type": "message"} 


def build_news():
    return True