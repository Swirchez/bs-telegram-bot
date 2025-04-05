from telethon import TelegramClient, events
import os

bot = TelegramClient(
    'bs_forwarder',
    int(os.getenv('API_ID')),
    os.getenv('API_HASH')
).start(bot_token=os.getenv('BOT_TOKEN'))

@bot.on(events.NewMessage(chats='@brawls_play'))
async def forward_posts(event):
    await bot.send_message(
        '@club_2VUPYJRCG',
        event.message,
        reply_to=227  # ID топика
    )
    print("Сообщение переслано!")

print("Бот запущен!")
bot.run_until_disconnected()