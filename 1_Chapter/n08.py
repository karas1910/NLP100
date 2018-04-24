import sys
sys.path.append("../../mymodule")
import mm

def cipher(data):
    ans = ""
    for s in data:
        if s.islower():
            ans += chr(219 - ord(s))
        else:
            ans += s
    return ans



if __name__ == '__main__':
    s = input()
    result1 = cipher(s)
    mm.chkprint(result1)
    result2 = cipher(result1)
    mm.chkprint(result2)

