import telebot
from telebot.async_telebot import AsyncTeleBot
import openai 
import asyncio
import time
user_requests = {}  # دیکشنری برای ذخیره تعداد درخواست‌های هر کاربر
request_limit = 15  # تعداد درخواست مجاز هر کاربر در بازه زمانی ۱۵ ثانیه
users_last_message_time = {}
bot = AsyncTeleBot('6243307595:AAH4cM-DQye23YFDtYlZQWR0Lbjz8KuJ414')
openai.api_key = "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"
@bot.message_handler(commands=['start'])
async def send_welcome(message):
  await bot.reply_to(message, "welcome to chat bot")
     
@bot.message_handler(func=lambda message: True)



async def kos_message(message):

    wait_message = await bot.reply_to(message, "please wait....")

    response = openai.Completion.create(
       model="text-davinci-003",
       prompt=f"chat bot{message.text}",
       #messages=message.text,
       temperature=0.5,
       max_tokens=256,
       top_p=1,
       frequency_penalty=0.0,
       presence_penalty=0.0,
    )
    await bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=wait_message.message_id,
        text=response.choices[0].text
    )
    
    
if __name__ == '__main__':
  import asyncio

asyncio.run(bot.polling())