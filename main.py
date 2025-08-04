import os
import sys
import time
import json
from player_date import get_player_status


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_hardware(hardware):
    hardware_lines = []
    for k, v in hardware.items():
        hardware_lines.append(f"  {k}: {v}")
    return "\n".join(hardware_lines)

with open(r'd:\MyFlie\code\ultimate-computer\player-date.json', 'r', encoding='utf-8') as f:
    data = json.load(f)



def print_main_screen():
    global player_status
    global version
    player_status = get_player_status(r'd:\MyFlie\code\ultimate-computer\player-date.json')
    version = data["Version"]
    clear_screen()
    print("=" * 38)
    print("  终极计算机 - ULTIMATE COMPUTER")
    print(f"  版本: {version}")
    print("=" * 38)
    print("【可用命令】")
    print("  1. status       查看玩家面板")
    print("  2. hardware     查看/升级硬件")
    print("  3. software     下载/管理软件包")
    print("  4. skill        查看/加点技能")
    print("  5. mission      查看/接取任务")
    print("  6. shop         商品商店")
    print("  7. help         帮助")
    print("  0. exit         退出游戏")
    print("=" * 38)

def main():
    while True:
        print_main_screen()
        choice = input("请输入命令: ").strip().lower()
        if choice in ['0', 'exit', 'quit']:
            print("感谢游玩终极计算机！")
            time.sleep(1)
            sys.exit(0)
        elif choice in ['1', 'status']:
             print(f"  计算机等级: {player_status['计算机等级']}   算力: {player_status['算力']}")
             print(f"  Git币: {player_status['Git币']}          软件包数: {player_status['软件包数量']}")
             print(f"  技能点: {player_status['技能点']}      当前任务: {player_status['当前任务']}")
             input("按回车键返回主界面")
        elif choice in ['2', 'hardware']:
            print(show_hardware(player_status["硬件"]))
            input("按回车键返回主界面")
        elif choice in ['3', 'software']:
            print("进入软件管理模块...（未实现）")
            input("按回车键返回主界面")
        elif choice in ['4', 'skill']:
            print("进入技能点管理模块...（未实现）")
            input("按回车键返回主界面")
        elif choice in ['5', 'mission']:
            print("进入任务系统模块...（未实现）")
            input("按回车键返回主界面")
        elif choice in ['6', 'shop']:
            print("进入商店...（未实现）")
            input("按回车键返回主界面")
        elif choice in ['7', 'help']:
            print("帮助信息：输入相应命令或编号进入模块。")
            input("按回车键返回主界面")
        else:
            print("无效命令，请重试！")
            time.sleep(1)

if __name__ == "__main__":
    main()