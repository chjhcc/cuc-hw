def func(listinfo):
    result = []
    for num in listinfo:
        if num % 2 == 0 and num < 100:
            result.append(num)
    return result

listinfo = [133, 88, 33, 22, 44, 11, 44, 55, 33, 22, 11, 11, 444, 66, 555]
output = func(listinfo)

assert isinstance(output, list), "输出类型错误"
assert all(isinstance(x, int) for x in output), "输出列表中的元素类型错误"
assert all(x % 2 == 0 and x < 100 for x in output), "输出列表中的元素不满足条件"

print(output)
