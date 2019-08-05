strs = ['alex', 'Lucy', 'dancy', 'Michael', 'lily']
# sorted()可以对序列(列表，元组等)进行排序,返回排序后的结果 原序列并没有变
# 按字母序(ASCII码 A:65 a:97)
print(sorted(strs))


# 可以通过key关键字 自定义排序方式
# 使用显式函数
def sort_func(x):
    return x[1].lower()  # 按照第2个字母小写的字母顺序进行排序


print(sorted(strs, key=sort_func))

# 使用匿名函数
print(sorted(strs, key=lambda x: x[2].upper()))  # 按照第3个字母大写的字母顺序进行排序
