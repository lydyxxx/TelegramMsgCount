from telethon import TelegramClient
from telethon.tl.types import User
import asyncio


api_id = ''
api_hash = ''
username_or_link = input('Input username link or @  > ')

async def count_messages():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    
    try:
        if username_or_link.startswith('t.me/'):
            username = username_or_link.split('/')[-1]
        else:
            username = username_or_link.replace('@', '')

        print(f"Ищем пользователя с username: {username}")
        
        user = await client.get_entity(username)

        if not isinstance(user, User):
            print("Указанный идентификатор не является пользователем")
            return

        print(f"Найден пользователь: {user.first_name} (ID: {user.id})")

        # Счетчики сообщений
        my_messages = 0
        their_messages = 0

        async for message in client.iter_messages(user):
            
            if message.sender_id == (await client.get_me()).id:
                my_messages += 1
            elif message.sender_id == user.id:
                their_messages += 1
        
        print(f"Статистика переписки с {user.first_name}:")
        print(f"Ваши сообщения: {my_messages}")
        print(f"Сообщения собеседника: {their_messages}")
        print(f"Всего сообщений: {my_messages + their_messages}")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    
    finally:
        await client.disconnect()

asyncio.run(count_messages())