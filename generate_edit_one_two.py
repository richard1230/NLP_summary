


def generate_edit_one(str):
    """
    给定一个字符串,生成编辑距离为1的字符串列表
    :param str:
    :return:
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(str[:i],str[i:]) for i in range (len(str) + 1)]          #这里的splites是个列表,inserts和deletes,replaces也是
    # print('-----------split')
    # print(splits)                                                       #[('', 'apple'), ('a', 'pple'), ('ap', 'ple'), ('app', 'le'), ('appl', 'e'), ('apple', '')]
    # print('-----------split')
    inserts = [L + c + R for L ,R in splits for c in letters]           #[a-z]apple,
    deletes = [L + R[1:] for L,R in splits if R]
    # print(deletes)                                                     #<class 'list'>: ['pple', 'aple', 'aple', 'appe', 'appl']
    replaces = [L + c + R[1:] for L,R in splits if R for c in letters ]

    # return set(inserts+deletes+replaces)
    # return set(deletes)
    return  set(replaces)
    # return set(inserts)
# print(len(generate_edit_one("apple")))

# print((generate_edit_one("apple")))

def generate_edit_two(str):
    """
    给定一个字符串，生成编辑距离不大于2的字符串
    :param str:
    :return:
    """
    return [e2 for e1 in generate_edit_one(str) for e2 in generate_edit_one(e1)]
# print(len(generate_edit_two("boy")))
print(generate_edit_two("boy"))

