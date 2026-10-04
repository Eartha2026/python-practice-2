# Day15.py 异常与调试
try:
    # 尝试执行可能会报错的代码
    数字1 = int(input("请输入被除数："))
    数字2 = int(input("请输入除数："))
    结果 = 数字1 / 数字2
    print(f"计算结果是：{结果}")
except ZeroDivisionError: # 捕获“除以零”的错误
    print("报错啦！除数不能为0！")
except ValueError: # 捕获“值错误”（比如输入了字母）
    print("报错啦！你输入的必须是纯数字！")
except Exception as 未知错误: # 兜底的错误捕获
    print(f"发生了未知错误：{未知错误}")

print("程序没有崩溃，继续往下跑！")