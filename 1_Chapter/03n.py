import re


if __name__ == '__main__':
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    s = re.sub(r'[,.]', '',s)
    s = s.split()

    ans = ''.join(str(len(i)) for i in s)
    print(ans)
