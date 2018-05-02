from n30 import sentence_mapping


def get_base_verb(target):
    result = []
    for t in target:
        for s in t:
            if s['pos'] == '動詞':
                result.append(s['base'])
    return result


if __name__ == '__main__':
    with open("./neko.txt.mecab") as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        target = sentence_mapping(sentenceL)
        result = get_base_verb(target)
        print(result)
