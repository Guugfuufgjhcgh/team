from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

api_id = '21205981'
api_hash = '7b5c43831fa6bfd470ca83d2796ad598'
phone_number = '+201289152099'

async def update_profile(client):
    while True:
        try:
            # الحصول على الوقت الحالي
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # تغيير اسم الحساب
            await client(UpdateProfileRequest(
                first_name=f'𝙂𝙃 {current_time}',
                last_name='𝙔𝙏'
            ))
            print("Profile name updated")

            # تغيير البايو
            await client(UpdateProfileRequest(
                about=f'𝙂𝙃 𝙔𝙏 .𝙥𝙮 {current_time}'
            ))
            print("Profile bio updated")

        except Exception as e:
            print(f"An error occurred: {e}")

        # انتظار ثانية واحدة قبل تحديث الوقت
        await asyncio.sleep(1)

async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        print("Client Created and Logged in")
        await update_profile(client)

asyncio.run(main())
