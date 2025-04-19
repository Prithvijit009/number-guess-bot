import random
from aiogram import types, Dispatcher
from utils.game_data import load_data, save_data
from utils.achievements import check_achievements
from utils.leaderboard_data import update_leaderboard

def register(dp: Dispatcher):
    @dp.message_handler(commands=['guess'])
    async def guess_game(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id not in data:
            data[user_id] = {
                "in_game": False,
                "games_played": 0,
                "wins": 0,
                "attempts": 0,
                "points": 0,
                "hint_used": False,
                "achievements": [],
                "coins": 0
            }
            save_data(data)
            await message.answer("❗ প্রথমে /start দিয়ে গেম শুরু করো।")
            return

        if "points" not in data[user_id]:
            data[user_id]["points"] = 0

        if not data[user_id]["in_game"]:
            number = random.randint(1, 100)
            data[user_id]["current_number"] = number
            data[user_id]["in_game"] = True
            data[user_id]["games_played"] += 1
            data[user_id]["attempts"] = 0
            data[user_id]["hint_used"] = False
            save_data(data)

            await message.answer(
                "🎉 Welcome to the Number Guessing Game!\n"
                "🔢 আমি ১ থেকে ১০০ এর মধ্যে একটা সংখ্যা ভেবেছি। তুমি কি সেটা ধরতে পারো?"
            )
        else:
            await message.answer("⚠️ তুমি ইতিমধ্যেই একটা গেমে আছো! আগে সেটা শেষ করো।")

    @dp.message_handler(lambda message: message.text.isdigit())
    async def handle_guess(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id in data and data[user_id]["in_game"]:
            if "points" not in data[user_id]:
                data[user_id]["points"] = 0

            try:
                guess = int(message.text)
            except ValueError:
                await message.answer("❗ সংখ্যাই দিতে হবে।")
                return

            correct = data[user_id]["current_number"]
            data[user_id]["attempts"] += 1

            if guess == correct:
                attempts = data[user_id]["attempts"]
                points = max(0, 10 - attempts)
                data[user_id]["wins"] += 1
                data[user_id]["in_game"] = False
                data[user_id]["points"] += points

                # ✅ Coins reward logic
                coins_earned = points
                if "coins" not in data[user_id]:
                    data[user_id]["coins"] = 0
                data[user_id]["coins"] += coins_earned

                # ✅ Leaderboard Update
                group_id = str(message.chat.id) if message.chat.type in ["group", "supergroup"] else None
                update_leaderboard(user_id=user_id, score=points, group_id=group_id)

                # ✅ Check Achievements
                check_achievements(user_id, data)

                save_data(data)
                await message.answer(
                    f"🎉 ঠিক ধরেছো! মোট {attempts} বার চেষ্টায় পেয়েছো। +{points} পয়েন্ট!\n"
                    f"🏅 মোট পয়েন্ট: {data[user_id]['points']}\n"
                    f"💰 মোট কয়েন: {data[user_id]['coins']}"
                )
            elif guess < correct:
                await message.answer("📉 কম হয়েছে! আরেকটু বড় দাও।")
            else:
                await message.answer("📈 বেশি হয়েছে! আরেকটু ছোট দাও।")

            save_data(data)

    @dp.message_handler(lambda message: not message.text.isdigit() and not message.text.startswith("/"))
    async def invalid_input(message: types.Message):
        data = load_data()
        user_id = str(message.from_user.id)

        if user_id in data and data[user_id]["in_game"]:
            await message.answer("❗️ সংখ্যায় উত্তর দাও, যেমন 27 বা 89।")
