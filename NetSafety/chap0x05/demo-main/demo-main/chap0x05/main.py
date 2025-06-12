from scapy.all import scapy, sr1, IP, ICMP
import socket

print("Scapy version: " + scapy.__version__)

# 目标 IP 地址
target_ip = 'www.cuc.edu.cn'

# 尝试解析目标 IP 地址
try:
    target_ip = socket.gethostbyname(target_ip)
except socket.gaierror:
    print(f"无法解析目标 IP 地址: {target_ip}")
    exit(1)

# 构造一个 ICMP echo request 包
icmp_packet = IP(dst=target_ip)/ICMP()

# 发送 ICMP echo request 包并接收响应
response = sr1(icmp_packet, timeout=2, verbose=0)

# 检查响应
if response is None:
    print(f"{target_ip} 无响应。网站可能离线。")
elif response.type == 0:
    print(f"{target_ip} 响应了 ICMP echo request。网站在线。")
else:
    print(f"收到来自 {target_ip} 的未知响应类型。")
