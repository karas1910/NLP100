from n30 import sentence_mapping


def get_noun_phrase(target):
    result = []
    for t in target:
        for i in range(1, len(t)-1):
            if t[i]['surface'] == 'の':
                if t[i-1]['pos'] == '名詞' and t[i+1]['pos'] == '名詞':
                    tmp = [t[i-1]['surface'], t[i]['surface'], t[i+1]['surface']]
                    result.append(tmp)
    return result


if __name__ == '__main__':
    with open('./neko.txt.mecab') as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result = get_noun_phrase(target)
        print(result)
