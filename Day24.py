# Day24.py TodoWrite（任务清单）
# 逻辑：把大任务拆解成小步骤，用进度条查看AI执行到哪了。
print("--- Day 24: TodoWrite 任务清单 ---")
CURRENT_TODOS = [
    {"content": "读取代码", "status": "completed"},
    {"content": "添加类型标注", "status": "in_progress"},
    {"content": "运行测试", "status": "pending"},
]
print("  ## 当前任务进度：")
for t in CURRENT_TODOS:
    icon = {"pending": "[ ]", "in_progress": "[▸]", "completed": "[✓]"}[t["status"]]
    print(f"  {icon} {t['content']}")
print("✅ 达成：把TodoList当进度条用。")