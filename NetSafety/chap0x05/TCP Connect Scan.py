import socket


def tcp_connect_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))  # connect_ex() returns 0 on success
    sock.close()
    return result == 0  # 0 means connection was successful, port is open


def scan_target(target, ports):
    for port in ports:
        if tcp_connect_scan(target, port):
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")


target_ip = '127.0.0.1'  # 替换为目标IP
ports_to_scan = [21, 22, 80, 443]  # 替换为你想扫描的端口列表
scan_target(target_ip, ports_to_scan)
