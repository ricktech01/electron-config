fillOrder = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p','6f']
elecInSL = {'s':2,'p':6,'d':10,'f':14}
fillOrderPos = [2, 4, 10, 12, 18, 20, 30, 36, 38, 48, 54, 56, 70, 80, 86, 88, 102, 112, 118, 132]


def getElecConf(e):
    final = ['']

    #temps
    c = 0
    i = 0
    eInO = 0
    while i < e:
        if i == fillOrderPos[c]:
            c +=1
            eInO = 0
            final.append('')
        eInO += 1
        final[c] = fillOrder[c] + str(eInO)
        i +=1
    print(final)
while (True):
    getElecConf(int(input('e:')))
