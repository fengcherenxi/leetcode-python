# 定义词频统计函数
def find_word(words,word_set):
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word]+=1
        else:
            words_count[word]=1
    return words_count

# 得到指定的文章的词表
words=[]
with open('find yourself.txt','r',encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace(',',' ')
        line = line.replace('.',' ')
        line = line.replace(':',' ')
        line = line.replace('!',' ')
        line = line.replace('?',' ')
        line = line.replace('\n',' ')
        line = line.replace('-',' ')
        line = line.replace('\'',' ')
        line = line.replace('"',' ')

        for word in line.split(' '):
            if word:
                words.append(word)
print(len(words))# 输出文章总词数
word_set = set(words)# 对词表进行去重
print(len(word_set))# 统计文章不同词数
print(find_word(words,word_set))# 统计词频        
