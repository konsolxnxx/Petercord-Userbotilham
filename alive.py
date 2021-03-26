from pyrogram import Filters
from userbot import bot

@bot.on_message(Filters.regex("^.alive"))
def amialivedad(event):
    chat = event.chat.id 
    message = " 𝐏𝐨𝐜𝐨𝐧𝐠 𝐎𝐧𝐥𝐞𝐧 User :)"
    bot.edit_message_text(chat_id=chat, message_id="me", text=message)
