import threading
from flask import Flask, send_from_directory
from flask_cors import CORS
import webview
import time
import os
import signal

# 创建 Flask 应用
app = Flask(__name__, template_folder='templates', static_folder='templates/static')
CORS(app)


@app.route('/')
def index():
    return send_from_directory('templates/static', 'index.html')


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('templates/static', path)


# 启动 Flask 服务器
def run_server():
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=False)


# 创建 PyWebview 窗口
def create_window():
    window = webview.create_window('Flask GUI', 'http://127.0.0.1:5000', width=800, height=600)
    webview.start()
    # 处理窗口关闭
    if server_thread.is_alive():
        os.kill(os.getpid(), signal.SIGTERM)  # 结束进程


# 全局变量用于控制 Flask 服务器线程
server_thread = None

if __name__ == '__main__':
    # 启动 Flask 服务器线程
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # 启动 PyWebview 窗口
    create_window()

    # 等待 Flask 服务器线程结束
    server_thread.join()

    print("Application has been closed.")
