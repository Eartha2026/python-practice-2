# Day12.py 命令行Todo List
任务列表 = [] # 用列表存所有的任务，每个任务是一个字典

def 显示任务():
    if not 任务列表:
        print("暂无任务。")
        return
    for i, 任务 in enumerate(任务列表): # enumerate可以同时拿到序号和内容
        状态 = "✅" if 任务["done"] else "❌" # 三元表达式
        print(f"{i+1}. [{状态}] {任务['name']}")

while True: # 死循环，不断接受输入
    cmd = input("\n请输入命令(add/list/done/del/quit): ")
    if cmd == "add":
        名字 = input("输入任务名：")
        任务列表.append({"name": 名字, "done": False}) # 加字典
    elif cmd == "list":
        显示任务()
    elif cmd == "done":
        序号 = int(input("输入完成的任务序号：")) - 1 # 索引从0开始
        任务列表[序号]["done"] = True
    elif cmd == "del":
        序号 = int(input("输入要删除的序号：")) - 1
        任务列表.pop(序号) # pop删除指定位置
    elif cmd == "quit":
        print("退出，再见！")
        break # 打破死循环