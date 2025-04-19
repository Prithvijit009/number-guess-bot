from aiogram import types, Dispatcher
from utils.game_data import load_data

def register(dp: Dispatcher):
    @dp.message_handler(commands=['stats'])
    async def show_stats(message: types.Message):
        print("📥 /stats command received")  # Debug

        data = load_data()
        user_id = str(message.from_user.id)

        if user_id not in data:
            await message.answer("❌ তুমি এখনো কোনো গেম খেলো নাই। /start দিয়ে শুরু করো।")
            return

        stats = data[user_id]
        await message.answer(
            f"📊 তোমার স্ট্যাটস:\n"
            f"🎮 মোট গেম খেলেছো: {stats.get('games_played', 0)}\n"
            f"🏆 মোট জিতেছো: {stats.get('wins', 0)}\n"
            f"📈 মোট চেষ্টার সংখ্যা: {stats.get('attempts', 0)}\n"
            f"💰 মোট পয়েন্ট: {stats.get('points', 0)}"
        )
