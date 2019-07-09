isContinue = True
while True:
    txt = input("enter a name")
    print(txt)
    for i in range(9):
        if str(i) in txt:
            print('not a name')
            isContinue = False
            break
    if isContinue:
        print("")
        break
            
            

    