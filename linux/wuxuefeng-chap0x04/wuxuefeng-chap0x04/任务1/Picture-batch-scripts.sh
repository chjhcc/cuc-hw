#!/bin/bash

# 定义帮助函数
function show_help {
    echo "Usage: $0 [options] [directory]"
    echo "Options:"
    echo "  -q <quality>       Compress JPEG images to quality (1-100)"
    echo "  -r <width>x<height> Resize images to specified dimensions while keeping aspect ratio"
    echo "  -w <text>         Add watermark text to images"
    echo "  -p <prefix>       Rename images with specified prefix"
    echo "  -s                Convert SVG and PNG images to JPEG"
    echo "  -h                Show this help message"
    exit 1
}

# 定义默认值
quality=100
resize=""
watermark=""
prefix=""
convert_to_jpg=false

# 解析命令行参数
while getopts ":q:r:w:p:sh" opt; do
    case $opt in
        q)
            quality=$OPTARG
            ;;
        r)
            resize=$OPTARG
            ;;
        w)
            watermark=$OPTARG
            ;;
        p)
            prefix=$OPTARG
            ;;
        s)
            convert_to_jpg=true
            ;;
        h)
            show_help
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            show_help
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            show_help
            ;;
    esac
done

# 移除已处理的参数
shift $((OPTIND-1))

# 检查是否指定了目录
if [ $# -lt 1 ]; then
    echo "No directory specified"
    show_help
fi

# 获取目录路径
directory=$1

# 检查目录是否存在
if [ ! -d "$directory" ]; then
    echo "Directory $directory does not exist"
    exit 1
fi

# 处理图片
find "$directory" -type f $-iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.svg"$-print0 | while IFS= read -r -d$'\0' file; do
    filename=$(basename -- "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"

    # 添加前缀
    if [ -n "$prefix" ]; then
        filename="$prefix$filename"
    fi

    # 转换为jpg
    if [ "$convert_to_jpg" = true ] && ([ "$extension" = "png" ] || [ "$extension" = "svg" ]); then
        convert "$file" "$directory/$filename.jpg"
        rm "$file"
        file="$directory/$filename.jpg"
        extension="jpg"
    fi

    # 压缩质量
    if [ -n "$quality" ] && [ "$extension" = "jpg" ]; then
        convert -quality "$quality" "$file" "$file"
    fi

    # 调整分辨率
    if [ -n "$resize" ]; then
        convert -resize "$resize" "$file" "$file"
    fi

    # 添加水印
    if [ -n "$watermark" ]; then
        composite -gravity southwest -geometry +10+10 -pointsize 20 -draw "text 0,0 '$watermark'" "$file" "$file"
    fi

    # 重命名文件
    if [ -n "$prefix" ] || [ "$convert_to_jpg" = true ]; then
        mv "$file" "$directory/$filename.$extension"
    fi
done

echo "All images processed."