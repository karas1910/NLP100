if __name__ == '__main__':
    with open("./neko.txt.mecab") as f:
        sentenceL = [s for s in f.read().split('EOS\n') if s != '']
        result = []

        for s in sentenceL:
            tmpL = []
            x  = s[:-1].split('\n')
            for l in x:
                surface, tail = l.split('\t')
                sp = tail.split(',')
                tmpL.append({'surface': surface, 'base': sp[6], 'pos': sp[0], 'pos1': sp[1]})
            result.append(tmpL)

        for i in result:
            if i[0]['pos1'] == 'サ変接続':
                print(i[0]['surface'])
