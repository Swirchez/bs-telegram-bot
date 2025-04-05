from telethon import TelegramClient, events
import os

bot = TelegramClient(
    'parser',
    int(os.getenv('API_ID')),  # УДАЛИТЬ ЭТУ СТРОКУ
    os.getenv('API_HASH')
).start(bot_token=os.getenv('BOT_TOKEN'))

async def main():
    print("Бот запущен! Мониторим канал...")
    channel = await bot.get_entity(os.getenv('SOURCE_CHANNEL'))
    print(f"Отслеживаем канал: {channel.title} (ID: {channel.id})")

    @bot.on(events.NewMessage(chats=channel))
    async def forward_posts(event):
        if not event.out:
            await bot.send_message(
                os.getenv('TARGET_GROUP'),
                event.message,
                reply_to=int(os.getenv('TOPIC_ID'))
            print(f"Переслано сообщение: {event.text[:50]}...")

    await bot.run_until_disconnected()

if __name__ == '__main__':
    bot.loop.run_until_complete(main())
