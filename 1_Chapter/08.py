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
    print(ans)



if __name__ == '__main__':
    s = input()
    cipher(s)
