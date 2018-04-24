if __name__ == '__main__':
    s1 = 'パトカー'
    s2 = 'タクシー'


    ans = "".join(i+j for i, j in zip(s1, s2))
    print(ans)
