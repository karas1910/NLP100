import re


if __name__ == '__main__':
    f = open('./jawiki-country.txt', 'r').readlines()

    dict = {}

    for i in range(len(f)):
        if "基礎情報" in f[i]:
            for j in range(i+1, len(f)):
                s = ''
                key = ''
                data = f[j].split()
                if data == []:
                    break
                if data[0][0] == '|':
                    n = 0
                    for k in range(len(data)):
                        n += 1
                        if data[k] == "=":
                            break
                        key += data[k]
                    for l in range(n, len(data)):
                        s += data[l]
                    dict[key[1:]] = s
        if f[i][0] == '}':
            break
        for i in dict:
            print(i, dict[i])

