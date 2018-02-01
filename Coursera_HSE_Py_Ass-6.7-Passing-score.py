fileInput = open('input.txt', 'r', encoding='utf8')
scoreList = []
k = int(fileInput.readline())
for line in fileInput:
    i = line.split()
    if int(i[-1]) >= 40 and int(i[-2]) >= 40 and int(i[-3]) >= 40:
        scoreList.append(int(i[-1]) + int(i[-2]) + int(i[-3]))
fileInput.close()
lenScoreLIst = len(scoreList)
scoreCount = []
tList = []
for item in scoreList:
    if item not in tList:
        tList.append(item)
        t = (scoreList.count(item), item)
        scoreCount.append(t)
scoreCount.sort(key=lambda x: -x[1])
lenScoreCount = len(scoreCount)


def minScore(lSL, lSC, k, sC):
    if lSL <= k:
        return 0
    elif sC[0][0] > k:
        return 1
    t = 0
    for i in range(0, lSC):
        t += sC[i][0]
        if t > k:
            return sC[i - 1][1]


print(minScore(lenScoreLIst, lenScoreCount, k, scoreCount))
