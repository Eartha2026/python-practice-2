# Day16.py 文件读写与日志统计
from pathlib import Path # 导入路径工具

# 1. 先自己造一个假的日志文件，用来测试
日志内容 = """2026-10-04 INFO 系统正常启动
2026-10-04 ERROR 登录失败，密码错误
2026-10-04 INFO 用户提交表单
2026-10-04 ERROR 网络超时
2026-10-04 ERROR 权限不足
2026-10-04 INFO 任务执行成功"""

# 用 with open 写文件，指定 encoding='utf-8'
with open("my_log.txt", "w", encoding="utf-8") as 文件:
    文件.write(日志内容)
print("日志文件写入成功！")

# 2. 读取文件并做统计
总行数 = 0
ERROR次数 = 0
最长的一行 = ""

with open("my_log.txt", "r", encoding="utf-8") as 文件:
    for 行 in 文件: # 逐行读取
        总行数 += 1
        行 = 行.strip() # 去掉末尾的换行符
        if "ERROR" in 行: # 包含 ERROR 关键字
            ERROR次数 += 1
        if len(行) > len(最长的一行): # 找最长的一行
            最长的一行 = 行

print(f"总行数：{总行数}")
print(f"ERROR 次数：{ERROR次数}")
print(f"最长的一行：{最长的一行}")