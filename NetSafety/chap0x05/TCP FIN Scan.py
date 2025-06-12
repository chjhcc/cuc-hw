import socket


def tcp_fin_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # 设置FIN标志
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    result = sock.connect_ex((target, port))
    sock.close()

    return result != 0  # 如果返回非0，表示端口开放


def scan_target_fin(target, ports):
    for port in ports:
        if tcp_fin_scan(target, port):
            print(f"Port {port} is open (FIN Scan).")
        else:
            print(f"Port {port} is closed.")


target_ip = '127.0.0.1'
ports_to_scan = [21, 22, 80, 443]
scan_target_fin(target_ip, ports_to_scan)
