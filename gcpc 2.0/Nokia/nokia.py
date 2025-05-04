def numtomsg(out):
    ctr = ""
    alpha = [[' '], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
             ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    out = out.split(" ")
    for i in out:
        if i[0] == "0":
            ctr = ctr + " "
        elif i[0] == "1":
            pass
        elif i[0] == "2":
            if (len(i) - 1) % 3 == 0:
                ctr = ctr + "a"
            elif (len(i) - 1) % 3 == 1:
                ctr = ctr + "b"
            elif (len(i) - 1) % 3 == 2:
                ctr = ctr + "c"

        elif i[0] == "3":
            if (len(i) - 1) % 3 == 0:
                ctr = ctr + "d"
            if (len(i) - 1) % 3 == 1:
                ctr = ctr + "e"
            if (len(i) - 1) % 3 == 2:
                ctr = ctr + "f"

        elif i[0] == "4":
            if (len(i) - 1) % 3 == 0:
                ctr = ctr + "g"
            if (len(i) - 1) % 3 == 1:
                ctr = ctr + "h"
            if (len(i) - 1) % 3 == 2:
                ctr = ctr + "i"
        elif i[0] == "5":
            if (len(i) - 1) % 3 == 0:
                ctr = ctr + "j"
            if (len(i) - 1) % 3 == 1:
                ctr = ctr + "k"
            if (len(i) - 1) % 3 == 2:
                ctr = ctr + "l"
        elif i[0] == "6":
            if (len(i) - 1) % 3 == 0:
                ctr = ctr + "m"
            if (len(i) - 1) % 3 == 1:
                ctr = ctr + "n"
            if (len(i) - 1) % 3 == 2:
                ctr = ctr + "o"
        elif i[0] == "7":
            if (len(i) - 1) % 4 == 0:
                ctr = ctr + "p"
            if (len(i) - 1) % 4 == 1:
                ctr = ctr + "q"
            if (len(i) - 1) % 4 == 2:
                ctr = ctr + "r"
            if (len(i) - 1) % 4 == 3:
                ctr = ctr + "s"

        elif i[0] == "8":
            if (len(i) - 1) % 4 == 0:
                ctr = ctr + "t"
            if (len(i) - 1) % 4 == 1:
                ctr = ctr + "u"
            if (len(i) - 1) % 4 == 2:
                ctr = ctr + "v"
        elif i[0] == "9":
            if (len(i) - 1) % 4 == 0:
                ctr = ctr + "w"
            if (len(i) - 1) % 4 == 1:
                ctr = ctr + "x"
            if (len(i) - 1) % 4 == 2:
                ctr = ctr + "y"
            if (len(i) - 1) % 4 == 3:
                ctr = ctr + "z"
            else:
                break
    print(ctr)


def msgtonum(x):
    num = ""
    for i in x:
        if i == ' ':
            num += "0 "

        if i == 'a':
            num += "2 "
        if i == 'b':
            num += "22 "
        if i == 'c':
            num += "222 "
        if i == 'd':
            num += "3 "
        if i == 'e':
            num += "33 "
        if i == 'f':
            num += "333 "
        if i == 'g':
            num += "4 "
        if i == 'h':
            num += "44 "
        if i == 'i':
            num += "444 "
        if i == 'g':
            num += "5 "
        if i == 'k':
            num += "55 "
        if i == 'l':
            num += "555 "
        if i == 'm':
            num += "6 "
        if i == 'n':
            num += "66 "
        if i == 'o':
            num += "666 "
        if i == 'p':
            num += "7 "
        if i == 'q':
            num += "77 "
        if i == 'r':
            num += "777 "
        if i == 's':
            num += "7777 "
        if i == 't':
            num += "8 "
        if i == 'u':
            num += "88 "
        if i == 'v':
            num += "888 "
        if i == 'w':
            num += "9 "
        if i == 'x':
            num += "99 "
        if i == 'y':
            num += "999 "
        if i == 'z':
            num += "9999 "
    print(num)


def nokia(func, input):
    if func == 1:
        numtomsg(input)
    elif func == 2:
        msgtonum(input)
    else:
        pass


a = int(input())
b = str(input())

nokia(a, b)