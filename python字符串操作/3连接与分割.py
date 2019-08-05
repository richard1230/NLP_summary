str1 = "大家好，我是Richard，太好了！"
str2 = '大家好，我是XXX，吃饭了吗？'
#使用+连接
print(str1+str2)        #大家好，我是Richard，太好了！大家好，我是XXX，吃饭了吗？
#使用join进行连接
#创建一个字符串列表
strs = ['我是Richard','我是XXX','太开心了，太棒了!']
print(';'.join(strs)) #使用;对列表中的各个字符串进行连接                    #我是Richard;我是XXX;太开心了，太棒了!
#join的反方法 split  进行切分
str3 = '我是Richard;我是XXX;太开心了，太棒了!'
print(str3.split(';')) #使用;对字符串进行切分 得到字符串列表                 #['我是Richard', '我是XXX', '太开心了，太棒了!']
