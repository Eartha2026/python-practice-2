# Day17.py 给 Todo List 加持久化（结合 Day 12 的内容）
import json
from pathlib import Path

文件名 = "todo.json"

# 1. 如果文件存在，就加载历史数据；如果不存在，就初始化一个空列表
if Path(文件名).exists():
    with open(文件名, "r", encoding="utf-8") as 文件:
        任务列表 = json.load(文件) # 变成Python的List和Dict
    print("已读取历史数据！")
else:
    任务列表 = []
    print("初次创建，暂无数据。")

# 2. 加入一些任务进行测试
任务列表.append({"name": "写Python作业", "done": False})
任务列表.append({"name": "背单词", "done": True})

# 3. 保存数据到 JSON 文件
with open(文件名, "w", encoding="utf-8") as 文件:
    json.dump(任务列表, 文件, ensure_ascii=False, indent=4)
    # ensure_ascii=False 保证中文不乱码；indent=4 保证排版好看（像一个规范的文档）
    
print("数据已持久化保存！重新运行此脚本，数据不会丢。")