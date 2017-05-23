import re


if __name__ == '__main__':
    f = open('./jawiki-country.txt').read()
    pattern = re.compile(r"{{基礎情報 国\n(.*)\n}}", re.S)
    matchOB = '\n'.join(pattern.findall(f))
    pattern = re.compile(r"\|(.*) = (.*)")
    ans = pattern.findall(matchOB)

    dict = {}
    for i in ans:
        print(i[0] + ' = ' + i[1])
        dict[i[0]] = i[1]
    print(dict)

