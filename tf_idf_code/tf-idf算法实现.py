
import nltk
import math
import string
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer

# text1 = "Python is a 2000 made-for-TV horror movie directed by Richard \
# Clabaugh. The film features several cult favorite actors, including William \
# Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy, \
# Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the \
# A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean \
# Whalen. The film concerns a genetically engineered snake, a python, that \
# escapes and unleashes itself on a small town. It includes the classic final\
# girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles, \
#  California and Malibu, California. Python was followed by two sequels: Python \
#  II (2002) and Boa vs. Python (2004), both also made-for-TV films."

text1 = "Python is a 2000 made-for-TV horror movie directed by Richard \
Clabaugh.Python was followed by two sequels: Python \
 II (2002) and Boa vs. Python (2004), both also made-for-TV films."

# text1 = "Natural language processing (NLP) is a field of computer science, artificial \
# intelligence and computational linguistics concerned with the interactions between computers\
#  and human (natural) languages, and, in particular, concerned with programming computers to fruitfully\
#   process large natural language corpora. Challenges in natural language processing frequently involve \
#   natural language understanding, natural language generation (frequently from formal, machine-readable \
#   logical forms), connecting language and machine perception, managing human-computer dialog systems, or \
#   some combination thereof."


text2 = "Python, from the Greek word (πύθων/πύθωνας), is a genus of \
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are \
recognised.[2] A member of this genus, P. reticulatus, is among the longest \
snakes known."

text3 = "The Colt Python is a .357 Magnum caliber revolver formerly \
manufactured by Colt's Manufacturing Company of Hartford, Connecticut. \
It is sometimes referred to as a \"Combat Magnum\".[1] It was first introduced \
in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued \
Colt Python targeted the premium revolver market segment. Some firearm \
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy \
Thompson, Renee Smeets and Martin Dougherty have described the Python as the \
finest production revolver ever made."

#分词
def get_tokens(text):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)     #punctuation:标点符号； string.punctuation 指的是所有的标点符号，ord用于返回字符串的ASCII碼
    # print(remove_punctuation_map)                                                       #string.punctuation:'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
                                                                                        #! 的ascii碼为34，"的ascii碼为35，#的ascii碼为35,上面一句的意思是说生成了一个字典,将所有的标点符号 与 None对应起来，
    no_punctuation = lowers.translate(remove_punctuation_map)                           #将字符串转移成 none
    # print(no_punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


tokens = get_tokens(text1)                                                              #分词
print(tokens)
count = Counter(tokens)                                                                 #Counter用于统计单词刷满的次数
print (count.most_common(10))                                                           #用于统计排在前10的单词

#去除停用词:
# tokens = get_tokens(text1)
filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)
# print (count.most_common(10))
# [('python', 5), ('films', 3), ('madefortv', 2), ('film', 2), ('california', 2), ('2000', 1), ('horror', 1), ('movie', 1), ('directed', 1), ('richard', 1)]


"""
像 films, film, filmed 其实都可以看出是 film，而不应该把每个词型都分别进行统计。这时就需要要用到 Stemming(词干提取,句子分解,提取主干) 方法。
1.按照规则剥离词缀，movie-->movi;
2.词形归并：识别非标准词，包括数字、缩写、日期以及映射任何此类词符到一个特殊的词汇
"""

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))                                  #movie-->movi;several--->sever
    return stemmed
tokens = get_tokens(text1)
filtered = [w for w in tokens if not w in stopwords.words('english')]
stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
# print(stemmed)
count = Counter(stemmed)
# print(count)
#Counter({'film': 6, 'python': 5, 'madefortv': 2, 'includ': 2, 'california': 2, '2000': 1, 'horror': 1, 'movi': 1, 'direct': 1, 'richard': 1, 'clabaugh': 1, 'featur': 1, 'sever': 1, 'cult': 1, 'favorit': 1, 'actor': 1, 'william': 1, 'zabka': 1, 'karat': 1, 'kid': 1, 'fame': 1, 'wil': 1, 'wheaton': 1, 'casper': 1, 'van': 1, 'dien': 1, 'jenni': 1, 'mccarthi': 1, 'keith': 1, 'coogan': 1, 'robert': 1, 'englund': 1, 'best': 1, 'known': 1, 'role': 1, 'freddi': 1, 'krueger': 1, 'nightmar': 1, 'elm': 1, 'street': 1, 'seri': 1, 'dana': 1, 'barron': 1, 'david': 1, 'bow': 1, 'sean': 1, 'whalen': 1, 'concern': 1, 'genet': 1, 'engin': 1, 'snake': 1, 'escap': 1, 'unleash': 1, 'small': 1, 'town': 1, 'classic': 1, 'finalgirl': 1, 'scenario': 1, 'evid': 1, 'like': 1, 'friday': 1, '13th': 1, 'lo': 1, 'angel': 1, 'malibu': 1, 'follow': 1, 'two': 1, 'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1})

# print("count,上面")
# print (count.most_common(10))
# [('film', 6), ('python', 5), ('madefortv', 2), ('includ', 2), ('california', 2), ('2000', 1), ('horror', 1), ('movi', 1), ('direct', 1), ('richard', 1)]


"""
上面为预处理
"""

#对一个文档而言，第一个word为:python
def tf(word, count):
    t1 = count[word]                #这里的count里面是个字典,count[word]指的就是python所对应的个数
    t2 = count.values()             #dict_values([3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),这里数字的个数与词语的个数是相等的(当然这里用的是修改之后的text1数据)
    t3 = sum(t2)                    #计算文本的总词数
    # print(count[word] / sum(count.values()))#这里计算的是词频
    return count[word] / sum(count.values())                                    #sum：把value加起来，count：有多少个value
#word:python
#count:Counter({'python': 3, 'madefortv': 2, '2000': 1, 'horror': 1, 'movi': 1, 'direct': 1, 'richard': 1, 'clabaughpython': 1, 'follow': 1, 'two': 1, 'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1, 'film': 1})



def n_containing(word, count_list):

    # print(sum(1 for count in count_list if word in count))                  #这里计算的是包含该词的文档总数,这里总共就三个文档，这里最大值也就是3了
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    # n1 = len(count_list)                                                    #这里计算的是文档的总数
    # print("上面是count_list的长度")
    # print(n1)
    # print(math.log(len(count_list) / (1 + n_containing(word, count_list))))
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))         #这里使用了类似于平滑的技术，计算出idf的值
#count_list里面有3个元素,每个元素都是每个文本里面的分词以及其对应出现的次数
#<class 'list'>: [Counter({'python': 3, 'madefortv': 2, '2000': 1, 'horror': 1, 'movi': 1, 'direct': 1, 'richard': 1, 'clabaughpython': 1, 'follow': 1, 'two': 1, 'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1, 'film': 1}), Counter({'genu': 2, 'python': 1, 'greek': 1, 'word': 1, 'πύθωνπύθωνας': 1, 'nonvenom': 1, 'pythons2': 1, 'found': 1, 'africa': 1, 'asia': 1, 'current': 1, '7': 1, 'speci': 1, 'recognised2': 1, 'member': 1, 'p': 1, 'reticulatu': 1, 'among': 1, 'longest': 1, 'snake': 1, 'known': 1}), Counter({'colt': 3, 'python': 3, 'revolv': 3, 'magnum': 2, 'manufactur': 2, '357': 1, 'calib': 1, 'formerli': 1, 'compani': 1, 'hartford': 1, 'connecticut': 1, 'sometim': 1, 'refer': 1, 'combat': 1, 'magnum1': 1, 'first': 1, 'introduc': 1, '1955': 1, 'year': 1, 'smith': 1, 'amp': 1, 'wesson': 1, 'm29': 1, '44': 1, 'discontinu': 1, 'target': 1, 'premium': 1, 'market': 1, 'segment': 1, 'firearm': 1, 'collector': 1, 'writer': 1, 'jeff': 1, 'cooper': 1, 'ian': 1, 'v': 1, 'hogg': 1, 'chuck': 1, 'hawk': 1, 'leroy': 1, 'thompson': 1, 'rene': 1, 'smeet': 1, 'martin': 1, 'dougherti': 1, 'describ': 1, 'finest': 1, 'product': 1, 'ever': 1, 'made': 1})]



def tfidf(word, count, count_list):
    # print(tf(word, count) * idf(word, count_list))
    return tf(word, count) * idf(word, count_list)



# countlist = [count1, count2, count3]
# for i, count in enumerate(countlist):
#     print("Top words in document {}".format(i + 1))
#     scores = {word: tfidf(word, count, countlist) for word in count}
#     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     for word, score in sorted_words[:3]:
#         print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


def count_term(text):
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count = Counter(stemmed)
    # print(count)
    # print("count 上面")
    # Counter({'film': 6, 'python': 5, 'madefortv': 2, 'includ': 2, 'california': 2, '2000': 1, 'horror': 1, 'movi': 1,
    #          'direct': 1, 'richard': 1, 'clabaugh': 1, 'featur': 1, 'sever': 1, 'cult': 1, 'favorit': 1, 'actor': 1,
    #          'william': 1, 'zabka': 1, 'karat': 1, 'kid': 1, 'fame': 1, 'wil': 1, 'wheaton': 1, 'casper': 1, 'van': 1,
    #          'dien': 1, 'jenni': 1, 'mccarthi': 1, 'keith': 1, 'coogan': 1, 'robert': 1, 'englund': 1, 'best': 1,
    #          'known': 1, 'role': 1, 'freddi': 1, 'krueger': 1, 'nightmar': 1, 'elm': 1, 'street': 1, 'seri': 1,
    #          'dana': 1, 'barron': 1, 'david': 1, 'bow': 1, 'sean': 1, 'whalen': 1, 'concern': 1, 'genet': 1, 'engin': 1,
    #          'snake': 1, 'escap': 1, 'unleash': 1, 'small': 1, 'town': 1, 'classic': 1, 'finalgirl': 1, 'scenario': 1,
    #          'evid': 1, 'like': 1, 'friday': 1, '13th': 1, 'lo': 1, 'angel': 1, 'malibu': 1, 'follow': 1, 'two': 1,
    #          'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1})
    # Counter({'genu': 2, 'python': 1, 'greek': 1, 'word': 1, 'πύθωνπύθωνας': 1, 'nonvenom': 1, 'pythons2': 1, 'found': 1,
    #          'africa': 1, 'asia': 1, 'current': 1, '7': 1, 'speci': 1, 'recognised2': 1, 'member': 1, 'p': 1,
    #          'reticulatu': 1, 'among': 1, 'longest': 1, 'snake': 1, 'known': 1})
    # Counter({'colt': 3, 'python': 3, 'revolv': 3, 'magnum': 2, 'manufactur': 2, '357': 1, 'calib': 1, 'formerli': 1,
    #          'compani': 1, 'hartford': 1, 'connecticut': 1, 'sometim': 1, 'refer': 1, 'combat': 1, 'magnum1': 1,
    #          'first': 1, 'introduc': 1, '1955': 1, 'year': 1, 'smith': 1, 'amp': 1, 'wesson': 1, 'm29': 1, '44': 1,
    #          'discontinu': 1, 'target': 1, 'premium': 1, 'market': 1, 'segment': 1, 'firearm': 1, 'collector': 1,
    #          'writer': 1, 'jeff': 1, 'cooper': 1, 'ian': 1, 'v': 1, 'hogg': 1, 'chuck': 1, 'hawk': 1, 'leroy': 1,
    #          'thompson': 1, 'rene': 1, 'smeet': 1, 'martin': 1, 'dougherti': 1, 'describ': 1, 'finest': 1, 'product': 1,
    #          'ever': 1, 'made': 1})

    return count


def main():
    texts = [text1, text2, text3]
    countlist = []
    for text in texts:
        countlist.append(count_term(text))                                              #分词,去掉停用词,词干提取等预处理之后的文本里面的词
        # print(countlist)
        # print("countlist上面")
        #[Counter({'film': 6, 'python': 5, 'madefortv': 2, 'includ': 2, 'california': 2, '2000': 1, 'horror': 1, 'movi': 1, 'direct': 1, 'richard': 1, 'clabaugh': 1, 'featur': 1, 'sever': 1, 'cult': 1, 'favorit': 1, 'actor': 1, 'william': 1, 'zabka': 1, 'karat': 1, 'kid': 1, 'fame': 1, 'wil': 1, 'wheaton': 1, 'casper': 1, 'van': 1, 'dien': 1, 'jenni': 1, 'mccarthi': 1, 'keith': 1, 'coogan': 1, 'robert': 1, 'englund': 1, 'best': 1, 'known': 1, 'role': 1, 'freddi': 1, 'krueger': 1, 'nightmar': 1, 'elm': 1, 'street': 1, 'seri': 1, 'dana': 1, 'barron': 1, 'david': 1, 'bow': 1, 'sean': 1, 'whalen': 1, 'concern': 1, 'genet': 1, 'engin': 1, 'snake': 1, 'escap': 1, 'unleash': 1, 'small': 1, 'town': 1, 'classic': 1, 'finalgirl': 1, 'scenario': 1, 'evid': 1, 'like': 1, 'friday': 1, '13th': 1, 'lo': 1, 'angel': 1, 'malibu': 1, 'follow': 1, 'two': 1, 'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1}), Counter({'genu': 2, 'python': 1, 'greek': 1, 'word': 1, 'πύθωνπύθωνας': 1, 'nonvenom': 1, 'pythons2': 1, 'found': 1, 'africa': 1, 'asia': 1, 'current': 1, '7': 1, 'speci': 1, 'recognised2': 1, 'member': 1, 'p': 1, 'reticulatu': 1, 'among': 1, 'longest': 1, 'snake': 1, 'known': 1}), Counter({'colt': 3, 'python': 3, 'revolv': 3, 'magnum': 2, 'manufactur': 2, '357': 1, 'calib': 1, 'formerli': 1, 'compani': 1, 'hartford': 1, 'connecticut': 1, 'sometim': 1, 'refer': 1, 'combat': 1, 'magnum1': 1, 'first': 1, 'introduc': 1, '1955': 1, 'year': 1, 'smith': 1, 'amp': 1, 'wesson': 1, 'm29': 1, '44': 1, 'discontinu': 1, 'target': 1, 'premium': 1, 'market': 1, 'segment': 1, 'firearm': 1, 'collector': 1, 'writer': 1, 'jeff': 1, 'cooper': 1, 'ian': 1, 'v': 1, 'hogg': 1, 'chuck': 1, 'hawk': 1, 'leroy': 1, 'thompson': 1, 'rene': 1, 'smeet': 1, 'martin': 1, 'dougherti': 1, 'describ': 1, 'finest': 1, 'product': 1, 'ever': 1, 'made': 1})]
        #上面有三个元素,每个元素以Counter开头;
    for i, count in enumerate(countlist):                                               #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        print("Top words in document {}".format(i + 1))
        # for word in count :
            # print(word)    对于document2:word指的是: python,greek,,word,genu等经过预处理的分词
            # print("上面是word")
        scores = {word: tfidf(word, count, countlist) for word in count}                #count：见下面一行
        #Counter({'film': 6, 'python': 5, 'madefortv': 2, 'includ': 2, 'california': 2, '2000': 1, 'horror': 1, 'movi': 1, 'direct': 1, 'richard': 1, 'clabaugh': 1, 'featur': 1, 'sever': 1, 'cult': 1, 'favorit': 1, 'actor': 1, 'william': 1, 'zabka': 1, 'karat': 1, 'kid': 1, 'fame': 1, 'wil': 1, 'wheaton': 1, 'casper': 1, 'van': 1, 'dien': 1, 'jenni': 1, 'mccarthi': 1, 'keith': 1, 'coogan': 1, 'robert': 1, 'englund': 1, 'best': 1, 'known': 1, 'role': 1, 'freddi': 1, 'krueger': 1, 'nightmar': 1, 'elm': 1, 'street': 1, 'seri': 1, 'dana': 1, 'barron': 1, 'david': 1, 'bow': 1, 'sean': 1, 'whalen': 1, 'concern': 1, 'genet': 1, 'engin': 1, 'snake': 1, 'escap': 1, 'unleash': 1, 'small': 1, 'town': 1, 'classic': 1, 'finalgirl': 1, 'scenario': 1, 'evid': 1, 'like': 1, 'friday': 1, '13th': 1, 'lo': 1, 'angel': 1, 'malibu': 1, 'follow': 1, 'two': 1, 'sequel': 1, 'ii': 1, '2002': 1, 'boa': 1, 'vs': 1, '2004': 1, 'also': 1})
        # print(scores)   #这里只写了text2的scores:
        #{'python': -0.013076457838717314, 'greek': 0.018430232186734747, 'word': 0.018430232186734747, 'πύθωνπύθωνας': 0.018430232186734747, 'genu': 0.036860464373469494, 'nonvenom': 0.018430232186734747, 'pythons2': 0.018430232186734747, 'found': 0.018430232186734747, 'africa': 0.018430232186734747, 'asia': 0.018430232186734747, 'current': 0.018430232186734747, '7': 0.018430232186734747, 'speci': 0.018430232186734747, 'recognised2': 0.018430232186734747, 'member': 0.018430232186734747, 'p': 0.018430232186734747, 'reticulatu': 0.018430232186734747, 'among': 0.018430232186734747, 'longest': 0.018430232186734747, 'snake': 0.0, 'known': 0.0}

        # print("上面是scores")
        #上面的这个scores就是一个字典,
        sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse=True)       #看上面的字典,python，greek等分词是在x[0]位置，这里匿名函数返回x[1],意思是说按照tfidf函数的返回值大小来降序排
        for word, score in sorted_words[:5]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))               #这里只排前5,round() 方法返回浮点数x的四舍五入值。


if __name__ == "__main__":
    main()
