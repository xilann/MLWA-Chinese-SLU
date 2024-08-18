import jieba
words=jieba.cut("帮我预定一家400-500价格区间的酒店")
for word in words:
    print(word)
