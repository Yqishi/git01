"""
请求地址：
1、请求一般的网页地址：
http://localhost:7890/ + 网页名称

2、ajax请求地址，获取数据：
http://localhost:7890/ajax_data?user=1  返回: {"name":"李思","age":18}
http://localhost:7890/ajax_data?user=2  返回: {"name":"王五","age":25}

3、jsonp请求地址，获取数据：
http://localhost:7890/jsonp_data?callback=fncall&user=1  返回: fncall({"name":"李思","age":18})
http://localhost:7890/jsonp_data?callback=fncall&user=2  返回: fncall({"name":"王五","age":25})
"""

import socket
import re
import sys


def main():
    """完成整体的控制"""

    if len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        else:
            print("端口号输入错误")
            return
    else:
        print("请以一下方式运行:python3 xxx.py 7890")
        return

    print("web服务器使用的端口是：%d" % port)


    # 1.创建tcp的套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定本地信息
    server_socket.bind(("", port))

    # 3. 将套接字变为监听套接字
    server_socket.listen(128)

    while True:
        # 4. 等待新用户
        new_socket, new_addr = server_socket.accept()

        # 5. 接收浏览器的请求
        request = new_socket.recv(1024).decode('utf-8')
        # print(request)
        if not request:
            new_socket.close()
            continue

        request_lines = request.splitlines()
        for i, line in enumerate(request_lines):
            print(i, line)

        # GET /login.html HTTP/1.1
        ret = re.match(r"([^/]*)/([^ ]*)", request_lines[0])
        if ret:
            print("当前请求方式：", ret.group(1))
            print("当前请求地址：", ret.group(2))
            # 提取需要的文件名(包含路径)
            file_name = ret.group(2)
            if file_name == "":
                file_name = "index.html"
            else:
                uarr = file_name.split('?')
                file_name = uarr[0]
                if(len(uarr)>1):
                    url_data = uarr[1]
                    print("当前请求参数：", url_data)

            if file_name == 'ajax_data':
                iNum = int(url_data.split('=')[1])
                if iNum == 1:
                    response_body = '{"name":"李思","age":18}'
                else:
                    response_body = '{"name":"王五","age":25}'

            if file_name == 'jsonp_data':
                arr = re.split('=|&', url_data)
                fnName = arr[1]
                uNum = int(arr[3])
                print('回调函数名是：' + fnName)
                if uNum == 1:
                    response_body = fnName + '('+'{"name":"李思","age":18}'+')'
                else:
                    response_body = fnName + '('+'{"name":"王五","age":25}'+')'

            if file_name == 'ajax_data' or file_name == 'jsonp_data':
                response_header = "HTTP/1.1 200 OK\r\n"
                response_header += "content-type:text/html; charset=utf-8\r\n"
                response_header += "\r\n"                
                response = response_header + response_body
                new_socket.send(response.encode("utf-8"))
                new_socket.close()
                continue

        
        # "index.html"
        try:
            f = open(file_name, "rb")
        except:
            response_header = "HTTP/1.1 404 Not Found\r\n"
            response_header += "content-type:text/html; charset=utf-8\r\n"
            response_header += "\r\n"
            response_body = "sorry, 么有你要找的文件...."

            response = response_header + response_body

            new_socket.send(response.encode("utf-8"))
        else:
            content = f.read()
            f.close()

            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "\r\n"
            response_body = content

            # 因为从文件读取出来的数据是二进制，而header是字符串，因此不能直接相加，需要分开发送
            # 先发送header
            new_socket.send(response_header.encode("utf-8"))
            # 再发送文件的数据(body)
            new_socket.send(response_body)

        finally:    
            new_socket.close()


if __name__ == "__main__":
    main()

