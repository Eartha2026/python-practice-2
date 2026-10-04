# import os
# from openai import OpenAI
# client = OpenAI(api_key="...", base_url="...") 

messages = [{"role": "system", "content": "你是一个助手"}]
print("欢迎使用DeepSeek聊天机器人！输入 'quit' 退出。")

while True:
    用户输入 = input("\n你：")
    if 用户输入 == "quit":
        break
    
    messages.append({"role": "user", "content": 用户输入})
    
    # 下面这段保持你刚才改的模拟输出不变！
    try:
        print("AI正在思考...")
        ai回复 = "我收到你的话了！这是模拟回复，因为环境问题，我先跑通逻辑打卡！"
        print(f"AI：{ai回复}")
        messages.append({"role": "assistant", "content": ai回复})
    except Exception as e:
        print(f"报错啦：{e}")
        messages.pop()