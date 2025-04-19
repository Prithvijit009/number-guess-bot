def check_achievements(user_id, data):
    user = data[user_id]
    achievements = user.get("achievements", [])

    # Example achievement: 5 wins
    if user.get("wins", 0) >= 5 and "Win 5 Games" not in achievements:
        achievements.append("Win 5 Games")

    # Example achievement: 10 points
    if user.get("points", 0) >= 10 and "Earn 10 Points" not in achievements:
        achievements.append("Earn 10 Points")

    # Save back the updated achievements list
    user["achievements"] = achievements
