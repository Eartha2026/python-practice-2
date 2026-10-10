# Day25.py Context Compact + System Prompt
# 逻辑：模拟AI的上下文压缩。AI会失忆，需要检查它是否记得核心要求。
print("--- Day 25: Context Compact + System Prompt ---")
# 1. 设定 System Prompt（给AI定规矩）
system_prompt = "你是一个Python助手，回答要简洁。"
print(f"设定System Prompt: {system_prompt}")
# 2. 模拟一段很长的对话
chat_history = ["用户闲聊1", "AI回答1", "用户闲聊2", "AI回答2", "核心要求：修复登录bug"]
print(f"压缩前，对话有 {len(chat_history)} 条记录。")
# 3. 模拟压缩（只保留核心要求）
compressed = ["核心要求：修复登录bug"]
print(f"压缩后，只保留核心记忆：{compressed}")
# 4. 检查记忆
if "核心要求：修复登录bug" in compressed:
    print("✅ 检查通过：AI还记得核心要求，没有跑偏。")
print("✅ 达成：亲眼见过上下文压缩，知道AI忘了的话要重申/开新会话。")