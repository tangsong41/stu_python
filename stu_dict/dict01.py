# 词典类型 dict
# 　　字典由键(key)和对应值(value)成对组成。字典也被称作关联数组或哈希表。
#
# 　　dict 赋值
#
# 　　dict 整体放在花括号{}中，每个键与值用冒号隔开（:），每对用逗号分割； d = {'one':1, 'two':2, 'three':3}
#
# 　　键必须独一无二，但值则不必；值可取任何数据类型，如字符串，数或元组；若创建时同一个键被赋值两次，后一个值会被记住；
#
# 　　键必须不可变，所以可以用数，字符串或元组充当，用列表就不行
#
# 　　用 dict() 强制转换，可接受以下形式，参见下例

# 复制代码
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
# 复制代码
#
#
# 　　dict 操作
#
# 　　　　词典类型适用于对应键的取值，十分实用；对于dict的访问、修改、增加、删除等操作需要熟练掌握
#
# 　　　　以下列出了常用的用法，详细请参考：
#
# 　　　　访问值、修改值
#
# 　　　　　　dict_name['key_name'] 可直接访问值，可直接更改该值
#
# 复制代码
d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(d['Name'],d['Age'],d['Class'])            # 访问键值访问 dict_name['key_name']
print("%s's age is %d, class is: %s." %(d['Name'], d['Age'],d['Class']))    # 字符串输出
# print(d['name'])                 # 无该键值，会报错，注意大小写
d['Age'] = 8
print(d['Age'])                    # 可直接修改键的数值，数值类型不限
# 复制代码
#
#
# 　　　　键的增加、删除
#
# 　　　　　　判断key是否存在于dict中，使用 key_name in/not in dict_name；
#
# 　　　　　　增加键值即对新的键赋值 dict_name['new key_name'] = value ；删除键值使用 del dict_name['key_name']；
#
# 　　　　　　清空词典使用 dict_name.clear()
#
# 复制代码
d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(d['Name'],d['Age'],d['Class'])            # 访问键值访问 dict['key_name']
print("%s's age is %d, class is: %s." %(d['Name'], d['Age'],d['Class']))    # 字符串输出
 # print(d['name'])                # 无该键值，会报错，注意大小写
d['Age'] = 8
print(d['Age'])                   # 可直接修改键的数值，数值类型不限
print('Name' in d)                # 判断键是否存在
print('xxx' not in d)             # 判断键是否不存在
d['Sex'] = "Female"               # 增加键值直接赋值即可
print(d)
del d['Class']                    # 删除键值
print(d)
# del d['Class']                  # 若无键值，会报错
d.clear()                         # 清空dict
print(d)

# 　　　　dict view objects
#
# 　　　　　　len(dict_name) 返回词典键值组合数，可单独取出所有键 dict_name.keys() ， 单独取出所有的值 dict_name.values()

d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(len(d))                    # 键值的组合数量
print(d.keys(),type(d.keys()))   # 为dict_keys 类型，可list()转换为list 或 set()转换为set
print(d.values())                # 为dict_values 类型
print(d.items())                 # 为dict_items 类型