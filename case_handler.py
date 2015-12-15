def updateDict(case, obj):
    obj = obj
    newCase = {}

    for i in case:
        if i != obj:
            newCase[i] = False
        elif i == obj:
            newCase[i] = True
    return newCase