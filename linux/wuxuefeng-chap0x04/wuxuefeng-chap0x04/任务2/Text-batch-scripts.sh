#!/bin/bash

# 脚本帮助信息函数
show_help() {
    echo "Usage: $0 [OPTION]..."
    echo "World Cup Data Processing Script"
    echo "  -h, --help             Display this help message"
    echo "  -f, --file <file>      Specify the data file to process"
    echo "  -y, --year <year>      Filter data by year"
    echo "  -t, --team <team>      Filter data by team"
    echo "  -p, --player <player>  Filter data by player"
    echo "  -g, --goals           Show goals scored by a player or team"
    echo "  -r, --results         Show match results"
    echo ""
    echo "Example: $0 -f worldcupdata.csv -y 1930 -t 'Brazil' -p 'Pele' -g"
    exit 0
}

# 确保数据文件存在
data_file="world_cup_players.txt"
if [ ! -f "$data_file" ]; then
    echo "Data file $data_file not found!"
    exit 1
fi

# 初始化变量
under_20=0
age_20_to_30=0
over_30=0

goalkeeper=0
defender=0
midfielder=0
forward=0

longest_name=""
longest_name_length=0
shortest_name=""
shortest_name_length=999

oldest_player=""
oldest_player_age=0
youngest_player=""
youngest_player_age=999

# 读取数据文件，进行统计
while IFS=',' read -r name age position; do
    # 根据年龄统计
    if ((age < 20)); then
        ((under_20++))
    elif ((age >= 20 && age <= 30)); then
        ((age_20_to_30++))
    else
        ((over_30++))
    fi

    # 根据位置统计
    case $position in
        "Goalkeeper") ((goalkeeper++)) ;;
        "Defender") ((defender++)) ;;
        "Midfielder") ((midfielder++)) ;;
        "Forward") ((forward++)) ;;
    esac

    # 最长和最短名字
    name_length=${#name}
    if ((name_length > longest_name_length)); then
        longest_name=$name
        longest_name_length=$name_length
    fi
    if ((name_length < shortest_name_length)); then
        shortest_name=$name
        shortest_name_length=$name_length
    fi

    # 最老和最年轻球员
    if ((age > oldest_player_age)); then
        oldest_player=$name
        oldest_player_age=$age
    fi
    if ((age < youngest_player_age)); then
        youngest_player=$name
        youngest_player_age=$age
    fi
done < "$data_file"

# 计算百分比
total_players=$((under_20 + age_20_to_30 + over_30))
percent_under_20=$(echo "scale=2; $under_20 / $total_players * 100" | bc)
percent_age_20_to_30=$(echo "scale=2; $age_20_to_30 / $total_players * 100" | bc)
percent_over_30=$(echo "scale=2; $over_30 / $total_players * 100" | bc)

# 输出结果
echo "Age < 20: $under_20 ($percent_under_20%)"
echo "Age 20-30: $age_20_to_30 ($percent_age_20_to_30%)"
echo "Age > 30: $over_30 ($percent_over_30%)"
echo
echo "Goalkeepers: $goalkeeper"
echo "Defenders: $defender"
echo "Midfielders: $midfielder"
echo "Forwards: $forward"
echo
echo "Longest name: $longest_name ($longest_name_length characters)"
echo "Shortest name: $shortest_name ($shortest_name_length characters)"
echo
echo "Oldest player: $oldest_player ($oldest_player_age years old)"
echo "Youngest player: $youngest_player ($youngest_player_age years old)"