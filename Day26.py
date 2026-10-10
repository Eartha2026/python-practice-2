# Day26.py Subagent 子智能体
# 逻辑：主Agent派小弟去干活，小弟干完把结果交回来。
print("--- Day 26: Subagent 子智能体 ---")
def run_subagent(task_name):
    print(f"  -> 派发子Agent去执行：{task_name}")
    print("  -> 子Agent拥有独立的上下文，不污染主对话...")
    print("  -> 子Agent执行完毕。")
    return f"【{task_name}】的结果数据"
# 主对话流程
print("主对话：用户询问项目状态。")
result = run_subagent("统计代码行数")
print(f"主Agent收到汇报：{result}，汇总完毕。")
print("✅ 达成：看懂了子Agent的派发、独立执行和结果汇合。")