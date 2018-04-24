def chkprint(*args):
    flg = 1
    for obj in args:
        for k, v in globals().items():
            if id(v) == id(obj):
                target = k
                break
        if flg == 1:
            out = target+' = '+str(obj)
            flg = 0
        else:
            out += ', '+target+' = '+str(obj)
    print(out)

if __name__ == '__main__':
    str1 = "paraparaparadise"
    str2 = "paragraph"
    X, Y = [], []

    for n in range(0, len(str1)-1):
        X.append(str1[n:n+2])
    for n in range(0, len(str2)-1):
        Y.append(str2[n:n+2])

    print("X = " + str(X))
    print("Y = " + str(Y))

    X, Y = set(X), set(Y)
    XuY = X | Y
    XnY = X & Y
    X_Y = X - Y
    Y_X = Y - X
    inx = 'se' in X
    iny = 'se' in Y

    chkprint(XuY)
    chkprint(XnY)
    chkprint(X_Y)
    chkprint(Y_X)
    chkprint(inx)
    chkprint(iny)


