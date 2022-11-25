from deep_translator import GoogleTranslator
from pyrogram import Client, filters
import Data



@Client.on_message(filters.private & filters.text, group=1)
async def translate(cl, me):
    if me.text == "/start" :
        await me.reply_text("اهلا بك انا بوت الترجمه !!")
    else :
        translator = GoogleTranslator('auto', 'ar') #من اي لغه الي اللغه العربيه
#       translator = GoogleTranslator('ar', 'en') 
        translated = translator.translate(me.text)
        await me.reply_text(translated)
        print(me.text)

