#!/bin/bash

# 脚本帮助信息函数
show_help() {
    echo "Usage: $0 [OPTION]..."
    echo "Server Log Processing Script"
    echo "  -h, --help             Display this help message"
    echo "  -f, --file <file>      Specify the log file to process"
    echo "  -i, --ip <ip>          Filter logs by IP address"
    echo "  -u, --user <user>      Filter logs by username"
    echo "  -d, --date <date>      Filter logs by date (format: YYYY-MM-DD)"
    echo "  -t, --time <time>      Filter logs by time (format: HH:MM:SS)"
    echo "  -e, --error           Show error logs only"
    echo "  -a, --access          Show access logs only"
    echo ""
    echo "Example: $0 -f server.log -i 192.168.1.1 -d 2023-04-01 -e"
    exit 0
}

# 默认值设置
log_file=""
ip_filter=""
user_filter=""
date_filter=""
time_filter=""
show_error=false
show_access=false

# 参数解析
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -h|--help)
            show_help
            ;;
        -f|--file)
            log_file="$2"
            shift 2
            ;;
        -i|--ip)
            ip_filter="$2"
            shift 2
            ;;
        -u|--user)
            user_filter="$2"
            shift 2
            ;;
        -d|--date)
            date_filter="$2"
            shift 2
            ;;
        -t|--time)
            time_filter="$2"
            shift 2
            ;;
        -e|--error)
            show_error=true
            shift
            ;;
        -a|--access)
            show_access=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            ;;
    esac
done

# 检查是否需要处理日志
if [[ -z "$log_file" ]]; then
    echo "No log file specified. Use -h for help."
    exit 1
fi

# 日志处理函数
process_logs() {
    # 根据IP地址过滤日志
    if [[ -n "$ip_filter" ]]; then
        grep "$ip_filter" "$log_file"
    fi
    
    # 根据用户名过滤日志
    if [[ -n "$user_filter" ]]; then
        grep "$user_filter" "$log_file"
    fi
    
    # 根据日期过滤日志
    if [[ -n "$date_filter" ]]; then
        grep "$date_filter" "$log_file"
    fi
    
    # 根据时间过滤日志
    if [[ -n "$time_filter" ]]; then
        grep "$time_filter" "$log_file"
    fi
    
    # 显示错误日志
    if $show_error; then
        grep "error" "$log_file"
    fi
    
    # 显示访问日志
    if $show_access; then
        grep "access" "$log_file"
    fi
}

# 调用日志处理函数
process_logs