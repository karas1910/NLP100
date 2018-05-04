from n30 import sentence_mapping


def get_max_noun_length(target):
    result = []
    for t in target:
        tmp = []
        for s in t:
            if s['pos'] == '名詞':
                tmp.append(s['surface'])
            elif tmp != []:
                result.append(tmp)
                tmp = []
    return result


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result = get_max_noun_length(target)
        print(result)
