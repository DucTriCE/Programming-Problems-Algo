
if __name__ == '__main__':
    s, t = list(input()), list(input())

    for i in range(len(s)-1, -1, -1):
        if s[i]=='z':
            s[i]='a'
        else:
            s[i]=chr(ord(s[i])+1)
            break

    if s!=t:
        print(''.join(s))
    else:
        print("No such string")