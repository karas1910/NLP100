if __name__ == '__main__':
    Seq = input('input:')
    spword = Seq.split(' ')
    result = []

    for i in range(0, len(spword)-1):
        result.append(spword[i:i + 2])

    print(result)
