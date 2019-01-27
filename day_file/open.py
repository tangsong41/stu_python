# coding:utf-8

# 一、读操作（r）
#
# 1.新建一个文件(去大理.txt)
# 文件内容：
# # 是不是对生活不太满意
# # 很久没有笑过又不知为何
# # 既然不快乐又不喜欢这里
# 不如一路向西去大理



# 2.读操作
f = open('D:\python\workspace\.py文件\去大理', encoding='utf8')            #绝对路径
data1 = f.read()
print(data1)
f.close()
# 返回值：
# 是不是对生活不太满意
# 很久没有笑过又不知为何
# 既然不快乐又不喜欢这里
# 不如一路向西去大理



f = open('D:\python\workspace\.py文件\去大理', encoding='utf8')
data2 = f.readable()            #判断是否可读
print(data2)
f.close()
#返回值：True



f = open('D:\python\workspace\.py文件\去大理', encoding = 'utf8')
data3 = f.readline()
data4 = f.readline()
data5 = f.readline()
print(data3)
print(data4)
print(data5)
f.close()
# 返回值：
# 是不是对生活不太满意
#
# 很久没有笑过又不知为何
#
# 既然不快乐又不喜欢这里



f = open('D:\python\workspace\.py文件\去大理', encoding = 'utf8')
data7 = f.readlines()
print(data7)
# 返回值：['是不是对生活不太满意\n', '很久没有笑过又不知为何\n', '既然不快乐又不喜欢这里\n', '不如一路向西去大理\n']
# 二、写操作（w）
#
# 1.新建一个文件(去大理.txt)
# 文件内容：
# 是不是对生活不太满意
# 很久没有笑过又不知为何
# 既然不快乐又不喜欢这里
# 不如一路向西去大理



# 2.写操作
f = open('D:\python\workspace\.py文件\上火星', 'w', encoding='utf8')
f.write('我要看火星人')
f.close()
# 返回值：
# ###一个新的.xtx文件，内容为：
# 我要看火星人



f = open('上火星', 'w', encoding='utf8')
data1 = f.writable()
print(data1)
f.close()
# 返回值：True



f = open('上火星', 'w', encoding='utf8')
f.writelines(['看月亮\n','玩扑克\n'])            #写多行新内容，覆盖光标后面的内容
f.close()

# 三、追加操作（a）

f = open('上火星', 'a', encoding='utf8')            #在最后一行追加
f.write('回地球')
# 四、其他操作（eg:r+）

f=open('D:\python\workspace\.py文件\上火星','r+',encoding='utf8')            #先读后写
data=f.read()
f.write('hi')
f.close()



f1 = open('上火星','r',encoding='utf8')
data = f1.readlines()
print(data)
f1.close()
f2 = open('上火星','w',encoding='utf8')            #修改原文件内容
f2.write(data[1])
f2.close()
# 五、读取日志文件的最后一行内容

# （1）创建一个日志文件.txt​
# 关键字      日期和时间          来源                事件ID  任务类别
# 审核成功	2018/9/11 12:17:15	Security-Auditing	4672	Special Logon
# 审核成功	2018/9/11 12:17:15	Security-Auditing	4624	Logon
# 审核成功	2018/9/11 12:17:14	Security-Auditing	4672	Special Logon
# 审核成功	2018/9/11 12:17:14	Security-Auditing	4624	Logon
# 审核成功	2018/9/11 12:17:07	Security-Auditing	4672	Special Logon
# 审核成功	2018/9/11 12:17:07	Security-Auditing	4624	Logon
# 审核成功	2018/9/11 12:09:27	Security-Auditing	4672	Special Logon
# 审核成功	2018/9/11 12:09:27	Security-Auditing	4624	Logon

​
# （2）用 seek()方法从后往前搜索​
f = open('日志文件','rb')
for i in f:
    offs = -70            #设置偏移量（估计最后一行长度）
    while True:
        f.seek(offs,2)
        data = f.readlines()
        if len(data) > 1:
            print(data[-1].decode('utf8'))
            break
        offs *=2
f.close()
# 返回：
# 审核成功	2018/9/11 12:09:27	Security-Auditing	4624	Logon
