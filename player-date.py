import json

with open('player-date.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# 获取玩家当前 CPU 型号
current_cpu = data['player_date']['硬件']['CPU']

# 查找当前 CPU 的算力
cpu_list = data['硬件信息']['CPU']
cpu_power = next((cpu['算力'] for cpu in cpu_list if cpu['型号'] == current_cpu), None)

print(f"当前CPU: {current_cpu}")
print(f"算力: {cpu_power}")