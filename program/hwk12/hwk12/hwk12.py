# 创建80x80的二维数组，并将所有元素初始化为0
arr = [[0 for _ in range(80)] for _ in range(80)]

# 遍历数组的行和列
for i in range(80):
    for j in range(80):
        # 如果行是偶数且列是奇数，或者行是奇数且列是偶数，则将该位置的元素赋值为1
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            arr[i][j] = 1

# 循环输出数组
while True:
    for row in arr:
        print("".join(str(x) for x in row))
