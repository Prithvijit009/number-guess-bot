
from aiogram import types, Dispatcher

def register(dp: Dispatcher):
    @dp.message_handler(commands=['about'])
    async def about(message: types.Message):
        await message.reply(
            "🤖 Number Guessing Game Bot\nCreated by @pritv9"
        )
