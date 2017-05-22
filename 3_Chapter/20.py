import json


if __name__ == '__main__':
    f = open('./jawiki-country.json', 'r').readlines()
    w = open('./jawiki-country.txt', 'w')

    for i in f:
        data = json.loads(i)
        if data['title'] == 'イギリス':
            w.write(data['text'])

