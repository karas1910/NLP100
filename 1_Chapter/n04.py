if __name__ == '__main__':
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    nm = {1, 5, 6, 7, 8, 9, 15, 16}
    str_dic = {}

    spstr = str.split(" ")
    for num, word in enumerate(spstr):
        if num in nm:
            str_dic[word[0:1]] = num
        else:
            str_dic[word[0:2]] = num

    print(str_dic)
