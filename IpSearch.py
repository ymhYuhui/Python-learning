import socket
from tkinter import W

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('1.1.1.1', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

if __name__ == '__main__':
    print(get_host_ip())


txtfile = open("D:\\pyIpTest.txt",W)
txtfile.write("My Ip is : \t")
txtfile.write(get_host_ip())

txtfile.close()