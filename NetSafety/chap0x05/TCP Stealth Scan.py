import socket
import os


def tcp_syn_scan(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        # Try to connect using the SYN flag
        sock.connect_ex((target, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def scan_target_syn(target, ports):
    for port in ports:
        if tcp_syn_scan(target, port):
            print(f"Port {port} is open (SYN Scan).")
        else:
            print(f"Port {port} is closed.")


target_ip = '127.0.0.1'  # 替换为目标IP
ports_to_scan = [21, 22, 80, 443]
scan_target_syn(target_ip, ports_to_scan)
