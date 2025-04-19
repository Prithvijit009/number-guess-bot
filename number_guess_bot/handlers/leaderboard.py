from aiogram import types
from aiogram.types import ParseMode
from aiogram.dispatcher import Dispatcher
from utils.leaderboard_data import load_leaderboard_data

async def leaderboard_handler(message: types.Message):
    data = load_leaderboard_data()

    global_leaderboard = data.get("global_leaderboard", [])
    if not global_leaderboard:
        await message.answer("❌ এখনো কোনো গ্লোবাল লিডারবোর্ড ডেটা নেই!")
        return

    leaderboard_text = "🌍 <b>Global Leaderboard - Top 10</b>\n\n"
    for idx, entry in enumerate(global_leaderboard[:10], start=1):
        leaderboard_text += f"{idx}. 🧑 User ID: <code>{entry['user_id']}</code> - {entry['score']} points\n"

    await message.answer(leaderboard_text, parse_mode=ParseMode.HTML)

def register(dp: Dispatcher):
    dp.register_message_handler(leaderboard_handler, commands=["leaderboard"])
