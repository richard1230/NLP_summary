str1 = "   hello world, hello, my name is Richard!  "
print(str1)
#去除首尾所有空格
print(str1.strip())
#去除首部所有空格
print(str1.lstrip())
#去除尾部所有空格
print(str1.rstrip())
#也可以去掉一些特殊符号
print(str1.strip().rstrip('!')) #方法可以组合使用 先去掉首尾空格 在去掉尾部!
#注意不能直接str.rstrip('!'),因为此时str的尾部是空格，得先去掉空格再去叹号。



#字符串替换
print(str1)
print(str1.replace('hello','how do you do')) #将所有hello都替换为hoe do you do
str2 = "  大家好，我是萌妹子, "
print(str2)
#去除空格和特殊符号
print(str2.strip().lstrip().rstrip(','))
#字符串替换
print(str2.replace('萌妹子','Richard'))
#替换为空串''  相当于删除
print(str2.replace('大家好，',''))
#    hello world, hello, my name is Richard!
#    how do you do world, how do you do, my name is Richard!
#   大家好，我是萌妹子,
# 大家好，我是萌妹子
#   大家好，我是Richard,
#   我是萌妹子,

