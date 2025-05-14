import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
#读取“1—3月入职员工信息.xlsx”文件4个工作表的数据
df = pd.read_excel('1—3月入职员工信息.xlsx', index_col=0, sheet_name=['1月', '2月', '3月', '1月员工补充信息'])
print('原始数据：\n', df)
#获取1月入职员工信息及其补充信息
df1_1, df1_2 = df['1月'], df['1月员工补充信息']
df2, df3 = df['2月'], df['3月']		#获取2月和3月入职员工信息
df1 = pd.merge(df1_1, df1_2)	#横向合并1月入职员工信息及其补充信息
#纵向合并1月、2月和3月入职员工信息
df_total = pd.concat([df1, df2, df3], ignore_index=True)
print('1—3月入职员工信息：\n', df_total)

