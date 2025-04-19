
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(__file__))
from handlers import start, about, guess, stats, hint, achievements, leaderboard
from constants import BOT_TOKEN

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Register Handlers
start.register(dp)
about.register(dp)
guess.register(dp)
stats.register(dp)
hint.register(dp)
achievements.register(dp)
leaderboard.register(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
