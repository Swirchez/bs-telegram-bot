from telethon import TelegramClient, events
import os

bot = TelegramClient(
    'parser',
    int(os.getenv('API_ID')),
    os.getenv('API_HASH')
).start(bot_token=os.getenv('BOT_TOKEN'))

async def main():
    # Проверяем подключение к API
    print("Бот запущен! Мониторим канал...")
    channel = await bot.get_entity(os.getenv('SOURCE_CHANNEL'))  # Получаем объект канала
    print(f"Отслеживаем канал: {channel.title} (ID: {channel.id})")

    @bot.on(events.NewMessage(chats=channel))
    async def forward_posts(event):
        if not event.out:  # Игнорируем исходящие сообщения
            await bot.send_message(
                os.getenv('TARGET_GROUP'),
                event.message,
                reply_to=int(os.getenv('TOPIC_ID'))
            print(f"Переслано сообщение: {event.text[:50]}...")  # Логируем первые 50 символов

    await bot.run_until_disconnected()

if __name__ == '__main__':
    bot.loop.run_until_complete(main())
