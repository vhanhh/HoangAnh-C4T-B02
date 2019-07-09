while True:
    txt = input("enter a yob?")
    print(txt)
    if txt.isdigit():
        print('a number')
        break
    else:
        print('not a number')

    print(2019-int(txt))