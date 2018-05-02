from n30 import sentence_mapping


def get_sahen_noun(target):
    result = []
    for t in target:
        for s in t:
            if s['pos1'] == 'サ変接続':
                result.append(s['surface'])
    return result


if __name__ == '__main__':
    with open("./neko.txt.mecab") as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result = get_sahen_noun(target)
        print(result)
