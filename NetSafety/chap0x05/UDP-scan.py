import socket


def udp_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)

    try:
        # 发送一个空的UDP数据包
        sock.sendto(b"", (target, port))
        sock.recvfrom(1024)  # 尝试接收响应
        return True  # 如果没有异常，端口是开放的
    except socket.timeout:
        return False  # 超时没有响应，端口可能是开放的
    except socket.error:
        return False  # 其他错误，端口关闭
    finally:
        sock.close()


def scan_target_udp(target, ports):
    for port in ports:
        if udp_scan(target, port):
            print(f"Port {port} is open (UDP Scan).")
        else:
            print(f"Port {port} is closed or filtered.")


target_ip = '127.0.0.1'
ports_to_scan = [53, 161, 123]
scan_target_udp(target_ip, ports_to_scan)
