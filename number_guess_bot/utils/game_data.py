import json
import os
from constants import PLAYER_DATA_PATH

def load_data():
    if not os.path.exists(PLAYER_DATA_PATH):
        return {}
    
    with open(PLAYER_DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Ensure that 'points', 'achievements', and 'coins' fields are present for all users
    for user_id in data:
        if 'points' not in data[user_id]:
            data[user_id]['points'] = 0
        if 'achievements' not in data[user_id]:
            data[user_id]['achievements'] = []
        if 'coins' not in data[user_id]:
            data[user_id]['coins'] = 0  # ✅ নতুন ফিল্ড: কয়েন

    return data

def check_achievements(user_id, data):
    achievements = data[user_id].get('achievements', [])

    # Example Achievement 1: Win 10 games
    if data[user_id]['wins'] >= 10 and 'Win 10 games' not in achievements:
        achievements.append('Win 10 games')

    # Example Achievement 2: Win 1 game
    if data[user_id]['wins'] >= 1 and 'Win 1 game' not in achievements:
        achievements.append('Win 1 game')

    # Example Achievement 3: First Attempt Win
    if data[user_id]['attempts'] == 1 and 'First Attempt Win' not in achievements:
        achievements.append('First Attempt Win')

    # Add any other achievements you want here...

    data[user_id]['achievements'] = achievements

def save_data(data):
    with open(PLAYER_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
