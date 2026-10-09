# Day20.py 环境变量与API基础
import os
from dotenv import load_dotenv

# 1. 加载 .env 文件里的密钥
load_dotenv() 
api_key = os.getenv("DEEPSEEK_API_KEY")

if api_key:
    print(f"读取成功！你的API Key前6位是：{api_key[:6]}...")
else:
    print("读取失败，请检查 .env 文件是否存在！")

# 2. 模拟 HTTP GET 和 POST 请求（用伪代码让你理解）
# GET请求：就像在浏览器输入网址拿网页
get_url = "https://api.example.com/get_data"
print(f"模拟向 {get_url} 发送 GET 请求...")

# POST请求：就像填完表单提交给服务器
post_data = {"model": "deepseek", "messages": [{"role": "user", "content": "你好"}]}
print(f"模拟向服务器发送 POST 请求，携带 JSON 数据：{post_data}")
import os
from dotenv import load_dotenv

# 1. 加载 .env 文件里的变量
load_dotenv()

# 2. 读取变量
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

# 3. 打印看看（自己电脑上调试看看就好，不要截图发出来）
print("密钥是否读到：", "读到了" if api_key else "没读到！检查.env")
print("API地址：", base_url)