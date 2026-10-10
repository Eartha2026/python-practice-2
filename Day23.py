# Day23.py Tool Use + Permission（安全日，三道闸门）
# 逻辑：模拟权限审批（R02纪律），知道什么直接批、什么必须拒绝。
print("--- Day 23: Tool Use + Permission 三道闸门 ---")
def check_permission(tool_name, command):
    # 闸门1：硬拒绝
    DENY_LIST = ["rm -rf /", "sudo", "shutdown"]
    for pattern in DENY_LIST:
        if pattern in command:
            return f"⛔ Blocked: 拒绝执行 '{pattern}'"
    # 闸门2/3：规则匹配 & 用户审批
    if tool_name == "bash" and "rm " in command:
        return "⚠ 需要用户审批: 潜在破坏性命令"
    return "✅ 允许执行"

print(f"  AI请求执行: rm -rf / -> {check_permission('bash', 'rm -rf /')}")
print(f"  AI请求执行: cat file.txt -> {check_permission('bash', 'cat file.txt')}")
print(f"  AI请求执行: rm temp.txt -> {check_permission('bash', 'rm temp.txt')}")
print("✅ 达成：建立了安全意识防线。")