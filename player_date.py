import json

def get_player_status(json_path='player-date.json'):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    player_status = {
        "计算机等级": data["player_date"]["等级"],
        "算力": data["player_date"]["算力"],
        "Git币": data["player_date"]["Git币"],
        "硬件": data["player_date"]["硬件"],
        "软件包数量": data["player_date"]["软件包数量"],
        "技能点": data["player_date"]["技能点"],
        "当前任务": data["player_date"]["当前任务"]
    }
    return player_status
