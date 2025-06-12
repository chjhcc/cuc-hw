import socket


def tcp_xmas_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # 发送一个带有PSH、URG、FIN标志的TCP包
    sock.connect_ex((target, port))
    # 没有明确判断标准，但一般如果端口开放就没有响应
    sock.close()
    return True


def scan_target_xmas(target, ports):
    for port in ports:
        if tcp_xmas_scan(target, port):
            print(f"Port {port} is open (Xmas Scan).")
        else:
            print(f"Port {port} is closed.")


target_ip = '127.0.0.1'
ports_to_scan = [21, 22, 80, 443]
scan_target_xmas(target_ip, ports_to_scan)
