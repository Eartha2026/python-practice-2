# Day20.py 环境变量与API基础
import os
from dotenv import load_dotenv

# 1. 加载 .env 文件里的变量
load_dotenv()

# 2. 读取变量
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

# 3. 打印看看（注意R03纪律：只检查状态，绝对不要打印密钥明文！）
print("密钥是否读到：", "读到了" if api_key else "没读到！检查.env")
print("API地址是否配置：", "已配置" if base_url else "未配置（使用默认）")

# 4. 模拟 HTTP GET 和 POST 请求（伪代码，帮助理解）
get_url = "https://api.example.com/get_data"
print(f"\n模拟向 {get_url} 发送 GET 请求...")

post_data = {"model": "deepseek", "messages": [{"role": "user", "content": "你好"}]}
print(f"模拟向服务器发送 POST 请求，携带 JSON 数据：{post_data}")

# 5. 聊天机器人主循环（Mock版）
messages = [{"role": "system", "content": "你是一个助手"}]
print("\n欢迎使用DeepSeek聊天机器人！输入 'quit' 退出。")

while True:
    用户输入 = input("\n你：")
    if 用户输入 == "quit":
        break
    
    messages.append({"role": "user", "content": 用户输入})
    
    try:
        print("AI正在思考...")
        # 模拟输出（因为环境DLL拦截，先用Mock数据跑通逻辑打卡）
        ai回复 = "我收到你的话了！这是模拟回复，因为环境问题，我先跑通逻辑打卡！"
        print(f"AI：{ai回复}")
        messages.append({"role": "assistant", "content": ai回复})
    except Exception as e:
        print(f"报错啦：{e}")
        messages.pop()