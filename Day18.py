# Day18.py 类型标注与现代代码
from dataclasses import dataclass

# 1. 给函数加类型标注
def 算平均分(成绩列表: list[int]) -> float: # 参数是整数列表，返回浮点数
    if not 成绩列表: # 如果列表为空
        return 0.0
    总分 = sum(成绩列表)
    return 总分 / len(成绩列表)

# 2. 使用 dataclass 极简定义类
@dataclass
class 学生:
    姓名: str # 冒号后面写类型
    分数: int

# 3. 试用
我的成绩 = [88, 95, 60]
平均分 = 算平均分(我的成绩)
print(f"平均分是：{平均分}")

学生1 = 学生("张三", 88) # 自动生成构造函数
print(f"学生姓名：{学生1.姓名}, 分数：{学生1.分数}")