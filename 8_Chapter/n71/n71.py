def jadge_stopword(word):
    with open('./nltk_data/corpora/stopwords/english') as stopWords:
        stopWords = [sw.strip() for sw in stopWords.readlines()]
        if word in stopWords:
            return True
        else:
            return False
