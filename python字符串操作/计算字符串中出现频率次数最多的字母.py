import re
from collections import Counter


##第一种方法
def get_max_value_v1(text):
    text = text.lower()
    result = re.findall('[a-zA-Z]',text)                #去掉列表中的符号
    count = Counter(result)
    count_list = list(count.values())
    max_value = max(count_list)
    max_list = []
    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    max_list = sorted(max_list)
    return max_list[0]

#version 2
from collections import Counter

def get_max_value(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]


#version 3
import string

def get_max_value2(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


str1= get_max_value_v1('aaaaabcdefg')
str2 = get_max_value('abcdbbb')
print(str1)
print(str2)
str22= get_max_value2('cdfffg')
print(str22)

