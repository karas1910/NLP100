from n30 import sentence_mapping


def get_verb(target):
    result = []
    for t in target:
        for s in t:
            if s['pos'] == '動詞':
                result.append(s['surface'])
    return result


if __name__ == '__main__':
    with open("./neko.txt.mecab") as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        result = get_verb(sentence_mapping(sentenceL))
        print(result)
