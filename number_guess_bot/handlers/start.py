from aiogram import types, Dispatcher
from utils.game_data import load_data, save_data
from constants import PLAYER_DATA_PATH

def register(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_game(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id not in data:
            data[user_id] = {
                "games_played": 0,
                "wins": 0,
                "current_number": 0,
                "in_game": False,
                "points": 0  # points field added here
            }

        save_data(data)

        await message.answer(
            "🎮 Welcome to the Number Guessing Game!\n"
            "Type /guess to start playing!"
        )
