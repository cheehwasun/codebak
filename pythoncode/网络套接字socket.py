#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-03 18:16:47
# @Author  : wb1768 (wb1768@163.com)
# @Link    : http://example.org
# @Version : $Id$

# socket_demo.py 套接字接口
# 协议: TCP/IP(3次握手,4次断开) UDP(直接发数据)
# 一台PC最多可开 65535 个端口

import socket
import os

# 地址簇
socket.AF_INET  # IPV4, (host, port), host:'luzhuo.me' / '127.0.0.1'
socket.AF_INET6  # IPV6, (host, port, flowinfo, scopeid); boolean = socket.has_ipv6 // 是否支持ipv6

# 套接字类型
socket.SOCK_STREAM  # tcp
socket.SOCK_DGRAM  # udp
socket.SOCK_RAW  # 原始套接字(可伪造IP地址,发起DDOS攻击)
socket.SOCK_RDM  # UDP,保证交付,但不保证顺序
socket.SOCK_SEQPACKET


HOST = 'localhost' # windows: '127.0.0.1' / 'localhost'; linux:0.0.0.0
PORT = 10086


def tcp_server():
    '''
    TCP服务端
    '''

    # 1. 实例化socket对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 可重用地址
    # 2. 绑定
    server.bind((HOST, PORT))  # 绑定
    # 3. 监听链接
    server.listen()
    while True:
        # 4. 接收一个连接
        conn, addr = server.accept()  # (阻塞等待)接收一个连接, 返回 连接对象 地址
        while True:
            # 5. 接收/发送数据 (接收数据(命令), 发送数据量, 接收反馈, 发送全部数据)
            data_bytes = conn.recv(1024)  # (阻塞)接收数据
            if not data_bytes:
                break  # 当client断开时,conn.recv不断的接收空信息
            data_str = data_bytes.decode("utf-8")
            print("接收到数据: {}".format(data_str))
            res_cmd_bytes = os.popen(data_str).read().encode("utf-8")
            if not res_cmd_bytes:
                res_cmd_bytes = b"success"
            conn.send(str(len(res_cmd_bytes)).encode("utf-8"))  # 不能发送空数据
            conn.recv(1024)  # 为避免粘包, 发送数据后接收下客户端的反馈
            conn.send(res_cmd_bytes)  # 每次发送的数据量与缓存有关
        # 6. 关闭连接, 释放资源
        conn.close()
    server.close()


def tcp_client(data):
    '''
    TCP客户端
    :param data: 字符串数据
    '''

    # 1. 实例化对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 连接服务端
    client.connect((HOST, PORT))  # 连接
    if not data:
        return
    data_bytes = data.encode("utf-8")
    # 3. 发送/接收数据 (发送数据, 接收反馈, 发送反馈, 接收全部数据)
    client.send(data_bytes)  # 发送数据, 发送的数据不能为空, 未发完的数据将放到缓冲区继续发
    res_count_bytes = client.recv(1024)  # 接收数据, 每次接收的数据量有限制, 限制大小与系统有关
    client.send(b"seccess")  # 给服务器反馈
    if not res_count_bytes:
        res_count_bytes = b'0'
    res_count_int = int(res_count_bytes.decode("utf-8"))
    res_size_int = 0
    size = 1024  # 默认接收量
    res_data = b""
    while res_size_int < res_count_int:
        count_res_surplus = res_count_int - res_size_int
        if count_res_surplus <= size:
            size = count_res_surplus
        data = client.recv(size)  # 接收剩余的数据
        res_size_int += len(data)
        res_data += data
    else:
        print("数据总量: {}".format(res_size_int))
        data_str = data.decode("utf-8")
        print("数据: {}".format(data_str))
    # 4. 关闭连接, 释放资源
    client.close()  # 关闭连接



def udp_server():
    '''
    UDP服务端
    '''
    # 1. 实例化对象
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 可重用地址
    # 2. 绑定
    server.bind((HOST, PORT))

    while True:
        # 3. 接收数据
        data, address = server.recvfrom(1024)
        data_str = data.decode("utf-8")
        print("接收到数据: ", data_str)
        res_cmd_bytes = os.popen(data_str).read().encode("utf-8")
        if not res_cmd_bytes:
            res_cmd_bytes = b"success"
        if len(res_cmd_bytes) > 65507:
            res_cmd_bytes = res_cmd_bytes[:65507]
        server.sendto(res_cmd_bytes, address)  # 发送的数据限制为: 65535 - IP头(20) - UDP头(8) = 65507bite, 超过则异常
    # 4. 关闭连接, 释放资源
    server.close()


def udp_client(data):
    '''
    UDP客户端
    :param data: 字符串数据
    '''

    # 1. 实例化对象
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if not data:
        return
    data_bytes = data.encode("utf-8")
    # 2. 发送/接收数据
    client.sendto(data_bytes, (HOST, PORT))
    res, addr = client.recvfrom(65507)
    print("接收到数据: ", res.decode("utf-8"))
    # 3. 关闭连接, 释放资源
    client.close()



def socket_func():
    sk = socket.socket()

    # === socket ===
    sk.connect(('127.0.0.1', 8080))  # 连接
    sk.connect_ex(('127.0.0.1', 8080))  # 同connect, 返回错误提示符, 成功:0, 失败:errno变量值
    sk_temp = sk.dup()  # 复制套接字
    conn, addr = sk.accept()  # 阻塞式接收一个连接
    sk.bind(('127.0.0.1', 8080))  # 绑定
    # socket.listen([backlog]) // 监听连接, backlog限制未接受连接数, 默认合理值
    sk.listen()
    sk.getpeername()  # 远程套接字地址
    sk.getsockname()  # 自己套接字地址
    # socket.send(bytes[, flags]) // 发送数据(注:不许发送空数据) flags:与Unix系统有关,默认0
    sk.send(b"datas")
    # socket.sendall(bytes[, flags]) // 同send
    sk.sendall(b"datas")
    # socket.sendfile(file, offset=0, count=None) // 发送文件, offset:从哪开始读, count:限制发送的总字节数
    sk.sendfile(open("file.txt", 'rb'))  # 实际发送的是文本里的内容
    # socket.sendto(bytes, address) // 发送数据, 未作远程套接字连接时使用
    # socket.sendto(bytes, flags, address)
    sk.sendto(b"datas", ('127.0.0.1', 8080))
    # socket.recv(bufsize[, flags]) // 接收数据, bufsize:限制接收数据量 (注:非设置1024就能接收到1024的数据量)
    bytes = sk.recv(1024)
    # socket.recvfrom(bufsize[, flags]) // 接收数据,返回 (bytes, addr)
    bytes, addr = sk.recvfrom(1024)
    sk.close()  # 关闭, 可用with自动关闭
    sk.shutdown(socket.SHUT_RD)  # 关闭连接(一半/两半) SHUT_RD:不许接收, SHUT_WR:不许发送, SHUT_RDWR:不许接收和发送
    fd = sk.detach()  # 置于关闭状态,返回文件描述符
    fd = sk.fileno()  # 获取文件描述符, 失败:-1
    sk.get_inheritable()  # Socket是否可继承
    # socket.makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None) // 返回与套接字关联的文件对象
    file = sk.makefile()

    sk.setblocking(True)  # 设置是否为阻塞式套接字, False:无阻塞(sock.settimeout(0.0)), True:阻塞(sock.settimeout(None))
    num = sk.gettimeout()  # 获取超时时间, 单位秒, 未设置None
    sk.settimeout(None)  # 阻塞套接字超时时间, 单位秒,非负, None:阻塞式, >=0:非阻塞式
    # socket.setsockopt(level, optname, value) // 设置套接字属性的值
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sk.family  # 地址簇
    sk.type  # 套接字类型
    sk.proto  # 套接字协议



    # === socket 异常 ===
    socket.error  # OSError
    socket.herror  # 地址转换错误, gethostbyname_ex()
    socket.gaierror  # 地址错误, getaddrinfo()
    socket.timeout  # 超时异常



    # === socket 功能函数 ===
    # 创建
    # socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) // 创建新的套接字; family:地址簇, type:套接字类型, proto:协议号, fileno:文件描述符
    sk = socket.socket()
    # ---
    # socket.socketpair([family[, type[, proto]]]) // 创建一对已连接的socket对象
    sk = socket.socketpair()
    # socket.fromfd(fd, family, type, proto=0) // 从文件描述符fd, 创建一个套接字
    sk = socket.fromfd(sk.detach(), socket.AF_INET, socket.SOCK_STREAM)

    # 连接
    # ---
    # socket.create_connection(address[, timeout[, source_address]]) // 连接互联网上侦听的TCP地址  address:(host, port), timeout:超时, source_address:(host, port)
    socket.create_connection(('localhost', 12345))

    # 获取信息
    strs = socket.gethostname()  # 获取主机名
    num = socket.getdefaulttimeout()  # 默认超时时间, 没有None
    socket.setdefaulttimeout(5)  # 设置默认超时时间, 单位秒

    # 转换
    strs = socket.gethostbyname('DESKTOP-S62UA6O')  # 将主机名转为ipv4地址
    host, hosts, ipaddrs = socket.gethostbyname_ex('DESKTOP-S62UA6O')  # 同gethostbyname
    host, hosts, ipaddrs = socket.gethostbyaddr('192.168.1.103')  # 同gethostbyname
    # socket.getnameinfo(sockaddr, flags) 根据flags翻译sockaddr, flags: NI_DGRAM / NI_NAMEREQD / NI_NOFQDN / NI_NUMERICHOST / NI_NUMERICSERV
    host, port = socket.getnameinfo(('192.168.1.103', 80), socket.NI_NUMERICHOST)
    # socket.getservbyname(servicename[, protocolname]) // 根据服务名获取端口号, protocolname: 'tcp' / 'udp'
    port = socket.getservbyname('http')
    # socket.getservbyport(port[, protocolname]) // 根据端口号获取服务名
    strs = socket.getservbyport(80)
    # socket.ntohl(x) // 将32位正整数从网络字节顺序转换为主机字节顺序
    # socket.ntohs(x) // 将16位正整数从网络转换为主机字节顺序
    # socket.htonl(x) // 将32位正整数从主机转换为网络字节顺序
    # socket.htons(x) // 将16位正整数从主机转换为网络字节顺序
    bytes_ip = socket.inet_aton('192.168.1.103')  # 将IPv4地址转换为32位二进制格式
    strs = socket.inet_ntoa(bytes_ip)  # 将32位二进制格式地址转为IPv4地址
    # socket.inet_pton(address_family, ip_string)
    bytes_ip = socket.inet_pton(socket.AF_INET, '192.168.1.103')  # 同inet_aton
    strs = socket.inet_ntop(socket.AF_INET, bytes_ip)  # 同inet_ntoa

    # ---
    # socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0) 将主机/端口转为创建套接字所需的所有参数(family, type, proto, canonname, sockaddr)
    lists = socket.getaddrinfo('luzhuo.me', 80, family=socket.AF_INET, type=socket.SOCK_STREAM)
    # socket.getfqdn([name]) // 名称的完全限定域名(主机名), 空为本机
    strs = socket.getfqdn('www.baidu.com')



if __name__ == "__main__":

    # TCP
    tcp_server()
    while 1:
        data = input("输入数据: ")
        tcp_client(data)

    # UDP
    udp_server()
    while 1:
        data = input("输入数据: ")
        udp_client(data)

    # socket_func()



# socketserver_demo.py 网络服务框架, 简化了socket的服务端编写, 是对socket的封装, 可进行多线程/多进程并发
# 客户端仍然使用socket

import socketserver

# 具体服务器类
# socketserver.TCPServer  # TCP协议
# socketserver.UDPServer  # UDP协议
# socketserver.UnixStreamServer  # Unix TCP
# socketserver.UnixDatagramServer  # Unix UDP

# 继承关系
# BaseServer
#     TCPServer
#         UnixStreamServer
#     UDPServer
#         UnixDatagramServer

# 服务类(1. 要实现服务, 必须从BaseRequesthandler派生类, 并重新定义handle()方法)
# socketserver.ForkingMixIn  # 混合类的分叉版本
# socketserver.ThreadingMixIn  # 混合类的线程版本
# 以下类是min-in类预定义的
# socketserver.ForkingTCPServer  # 多进程 (Linux可用, Windows不可用)
# socketserver.ForkingUDPServer
# socketserver.ThreadingTCPServer  # 多线程
# socketserver.ThreadingUDPServer

HOST, POST = "localhost", 10086


# 所有请求处理对象的超类,他定义了接口
class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 一个连接调用一次handle()
        print(self.__dict__)
        # 与client的交互全都在这里完成
        while 1:
            try:
                data = self.request.recv(1024).strip()  # 接收数据
                ip = self.client_address[0]  # IP
                print("IP: {}, 数据: {}".format(ip, data.decode('utf-8')))
                self.request.sendall(b"success")  # 发送数据
            except ConnectionResetError as e:  # 客户端断开
                print("客户端断开连接")
                break

    def setup(self):
        # handle()调用之前,所需的初始化操作
        pass

    def finish(self):
        # handle()调用之后,所需的清理操作, setup()异常不会调用该函数
        pass


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()  # 接收数据
        socket = self.request[1]
        ip = self.client_address[0]  # IP
        print("IP: {}, 数据: {}".format(ip, data.decode('utf-8')))
        socket.sendto(b"success", self.client_address)



def socketserver_demo():
    '''
    1. 创建handler类,继承BaseRuestHandler,重写handler()
    2. 实例化server类(TCPServer), 传递ip和handler传给服务类
    3. server类.serve_forever()[处理多个请求] / .handler_request()[处理单个请求]
    4. server类.server_close() 关闭socket
    '''

    # TCP
    # server = socketserver.TCPServer((HOST, POST), ServerHandler)  # 单线程
    server = socketserver.ThreadingTCPServer((HOST, POST), TCPHandler)  # 多线程, 每次新的连接都会开启新线程
    # server.handle_request()  # 处理单个请求
    server.serve_forever()  # 处理多个请求

    # UDP
    # server = socketserver.UDPServer((HOST, POST), ServerHandler)  # 单线程
    server = socketserver.ThreadingUDPServer((HOST, POST), UDPHandler)  # 多线程, 每次新的连接都会开启新线程
    # server.handle_request()  # 处理单个请求
    server.serve_forever()  # 处理多个请求



def socketserver_func():
    # 2. 创建服务类
    # class socketserver.BaseServer(server_address, RequestHandlerClass) // 所有服务类对象的超类, 他定义了接口
    server = socketserver.TCPServer((HOST, POST), TCPHandler)

    fd = server.fileno()  # 文件描述符
    server.handle_request()  # 处理单个请求, hanle()引发一场调用handle_error(), 超时调用handle_timeout()
    # serve_forever(poll_interval=0.5) // 处理多个请求,直到显式的shutdown()请求, 每poll_interval秒关闭poll
    server.serve_forever()
    server.service_actions()  # 在serve_forever()循环中调用, 可用于清理数据
    server.shutdown()  # 告知serve_forever()停止并等待
    server.server_close()  # 清理服务器
    server.address_family  # 地址簇
    request = server.RequestHandlerClass  # 请求处理类, 为每个请求创建此类
    host, port = server.server_address  # 服务器正在侦听的地址
    socket = server.socket  # 套接字对象

    boolean = server.allow_reuse_address  # 服务器是否允许重用地址
    size = server.request_queue_size  # 请求队列的大小, 默认5个, 队列已满,下个请求将获得'连接被拒绝'错误
    type = server.socket_type  # 套接字类型
    time = server.timeout  # 超时时间, 单位秒, None:阻塞式, 0.0:非阻塞式
    # server.finish_request(request, client_address) // handle(self), self:{'request': ..., 'client_address': ..., 'server': ...}
    server.finish_request(request, (HOST, POST))  # handle()请求
    server.handle_error(request, (HOST, POST))  # handle()异常
    server.handle_timeout()  # handle()超时
    server.process_request(request, (HOST, POST))  # handle()请求, 如有必要创建新进程/线程处理请求
    boolean = server.verify_request(request, (HOST, POST))  # handle()是否可请求, True处理请求,False拒绝请求
    socket, addrs = server.get_request()  # 获取套接字请求(会阻塞,直至新的连接), 返回新套接字对象和客户端地址
    server.server_activate()  # 监听, 同listen()
    server.server_bind()  # 绑定


if __name__ == "__main__":
    socketserver_demo()

    # socketserver_func()    
