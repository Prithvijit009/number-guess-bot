# utils/leaderboard_data.py

import json
import os
from constants import LEADERBOARD_DATA_PATH

def load_leaderboard_data():
    if not os.path.exists(LEADERBOARD_DATA_PATH):
        return {
            "global_leaderboard": [],
            "global_weekly_leaderboard": [],
            "global_monthly_leaderboard": [],
            "group_leaderboards": {}
        }

    with open(LEADERBOARD_DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_leaderboard_data(data):
    with open(LEADERBOARD_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_leaderboard(user_id, score, group_id=None):
    data = load_leaderboard_data()

    global_leaderboard = data["global_leaderboard"]
    global_leaderboard.append({"user_id": user_id, "score": score})
    global_leaderboard = sorted(global_leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    data["global_leaderboard"] = global_leaderboard

    weekly_leaderboard = data["global_weekly_leaderboard"]
    weekly_leaderboard.append({"user_id": user_id, "score": score})
    weekly_leaderboard = sorted(weekly_leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    data["global_weekly_leaderboard"] = weekly_leaderboard

    monthly_leaderboard = data["global_monthly_leaderboard"]
    monthly_leaderboard.append({"user_id": user_id, "score": score})
    monthly_leaderboard = sorted(monthly_leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    data["global_monthly_leaderboard"] = monthly_leaderboard

    if group_id:
        if group_id not in data["group_leaderboards"]:
            data["group_leaderboards"][group_id] = {
                "weekly": [],
                "monthly": [],
                "top_10": []
            }
        group = data["group_leaderboards"][group_id]
        group["weekly"].append({"user_id": user_id, "score": score})
        group["weekly"] = sorted(group["weekly"], key=lambda x: x['score'], reverse=True)[:10]
        group["monthly"].append({"user_id": user_id, "score": score})
        group["monthly"] = sorted(group["monthly"], key=lambda x: x['score'], reverse=True)[:10]
        group["top_10"] = sorted(group["weekly"] + group["monthly"], key=lambda x: x['score'], reverse=True)[:10]
        data["group_leaderboards"][group_id] = group

    save_leaderboard_data(data)
