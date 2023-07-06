from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

# 打开JSON文件
with open('value1.json', 'r') as file:
    # 读取文件内容
    value1 = json.load(file)
with open('value2.json', 'r') as file:
    # 读取文件内容
    value2 = json.load(file)
with open('value3.json', 'r') as file:
    # 读取文件内容
    value3 = json.load(file)

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析URL并提取参数
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
         # 获取参数值
        param_value = query_params.get('param', [''])[0]
         # 根据参数值生成JSON数据
        if param_value == 'value1':
            data = value1
        elif param_value == 'value2':
            data = value2
        else:
            data = value3
         # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
         # 发送JSON数据作为响应
        self.wfile.write(json.dumps(data).encode())
def run_server():
    server_address = ('', 8888)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Starting server...')
    httpd.serve_forever()
run_server()