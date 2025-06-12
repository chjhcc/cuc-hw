import socket


def tcp_null_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # 发送没有任何标志的TCP包
    result = sock.connect_ex((target, port))
    sock.close()

    return result != 0  # 返回非0表示端口开放


def scan_target_null(target, ports):
    for port in ports:
        if tcp_null_scan(target, port):
            print(f"Port {port} is open (Null Scan).")
        else:
            print(f"Port {port} is closed.")


target_ip = '127.0.0.1'
ports_to_scan = [21, 22, 80, 443]
scan_target_null(target_ip, ports_to_scan)
