#!/usr/bin/env python3
"""Launcher menu for PRContentBot.

Run this script (set as .replit run command) to choose which workflow
to execute on Replit or local environment.
"""

import subprocess, sys, os

MENU = {
    "1": ("抓取 Twitter+Reddit 并精选 30 条", "python3 main_fetch_social.py"),
    "2": ("抓取新闻 RSS 并精选 30 条", "python3 main_fetch_news.py"),
    "3": ("根据手工编辑的 Excel 逐条生成公众号文章", "python3 main_generate_from_excel.py"),
    "4": ("生成社交平台热帖合辑文章", "python3 main_generate_hotdigest.py"),
    "q": ("退出", None),
}

def show_menu():
    print("\n====== PRContentBot Launcher ======")
    for k, v in MENU.items():
        print(f"{k}. {v[0]}")
    print("===================================\n")

def main():
    while True:
        show_menu()
        choice = input("请选择任务编号 (q 退出): ").strip()
        if choice.lower() == "q":
            print("Bye!")
            break
        cmd = MENU.get(choice, (None, None))[1]
        if not cmd:
            print("无效选择，请重新输入\n")
            continue
        print(f"\n>>> 运行: {cmd}\n")
        res = subprocess.run(cmd, shell=True)
        if res.returncode != 0:
            print("脚本执行出现错误\n")
        input("\n任务完成，按回车键返回菜单...")

if __name__ == "__main__":
    main()
