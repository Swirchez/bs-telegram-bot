from telethon import TelegramClient, events
import os

bot = TelegramClient(
    'anon_forwarder',
    int(os.getenv('API_ID')),
    os.getenv('API_HASH')
).start(bot_token=os.getenv('BOT_TOKEN'))

@bot.on(events.NewMessage(chats=os.getenv('SOURCE_CHANNEL')))
async def handle_new_message(event):
    await bot.send_message(
        entity=os.getenv('TARGET_GROUP'),
        message=event.text,
        file=event.media,
        formatting_entities=event.message.entities,
        link_preview=not event.message.web_preview,
        reply_to=int(os.getenv('TOPIC_ID'))  # Убрал silent для стандартных уведомлений
    )

if __name__ == '__main__':
    print("Бот запущен!")
    print(f"Отслеживаем канал: {channel.title} (ID: {channel.id})")
    bot.run_until_disconnected()
