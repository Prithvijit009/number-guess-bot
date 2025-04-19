from aiogram import types, Dispatcher
from utils.game_data import load_data, save_data

def register(dp: Dispatcher):
    @dp.message_handler(commands=['hint'])
    async def give_hint(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id not in data or not data[user_id].get("in_game", False):
            await message.reply("⚠️ এখন কোনো গেম চলছে না! /guess দিয়ে গেম শুরু করো।")
            return

        if data[user_id].get("hint_used", False):
            await message.reply("💡 তুমি এই রাউন্ডে ইতিমধ্যেই হিন্ট নিয়েছো!")
            return

        number = data[user_id]["current_number"]

        low = number - (number % 5)
        high = low + 5
        if high > 100:
            high = 100
        if low < 1:
            low = 1

        await message.reply(f"💡 হিন্ট: সংখ্যা {low} এবং {high} এর মধ্যে!")

        data[user_id]["hint_used"] = True
        save_data(data)
