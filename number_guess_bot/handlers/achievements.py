from aiogram import types, Dispatcher
from utils.game_data import load_data

def register(dp: Dispatcher):
    @dp.message_handler(commands=['achievements'])
    async def show_achievements(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id not in data:
            await message.answer("❌ তুমি এখনো কোনো গেম খেলো নাই। /start দিয়ে শুরু করো।")
            return

        achievements = data[user_id].get("achievements", [])
        
        if not achievements:
            await message.answer("😅 এখনো কোনো achievement পাও নি! চেষ্টা চালিয়ে যাও 💪")
        else:
            msg = "🏆 তোমার অর্জিত Achievements:\n\n"
            for ach in achievements:
                emoji = {
                    "first_win": "🥇",
                    "five_games": "🎮",
                    "perfect_game": "💯",
                    "point_master": "💰"
                }.get(ach, "⭐")

                msg += f"{emoji} {ach.replace('_', ' ').title()}\n"
            
            await message.answer(msg)
