def updateDict(case, obj):
    obj = obj

    newCase = {}
    for i in case:
        print(i)
        if i != obj:
            newCase[i] = False
        elif i == obj:
            newCase[i] = True
    print(newCase)
    return newCase