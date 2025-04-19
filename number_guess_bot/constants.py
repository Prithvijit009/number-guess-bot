
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = "@pritv9"
PLAYER_DATA_PATH = "players.json"
# Path to the leaderboard data JSON file
LEADERBOARD_DATA_PATH = "data/leaderboard.json"


