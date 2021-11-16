def encodeInDSP(n):
    res = ""
    symbCount = 0
    if n == 0:
        res = a1[0]
        symbCount+=1
    while n:
        res+=a1[int(n%3)]
        n//=3
        symbCount+=1
    if symbCount < 4:
        res+=(4 - symbCount) * a1[0]
    return res


def fillDictionary():
    global a, a1, a2
    a = " йцукенгшщзхъфывапролджэячсмитьбюё,.!"
    a2 = {}
    for i in range(0, 37):
        a2[a[i]] = encodeInDSP(i)
        print(a[i], a2[a[i]])


def encode(s):
    for i in s:
        print(a2[i], end=" ")


a1 = "д с п".split(" ")
a1 = "Денис Сергеевич Подкопаев".split(" ")
fillDictionary()

s = "Здравствуйте Денис Сергеевич! Могу вас заверить, что новый год буду встречать в маске и перчатках.".lower()
encode(s)
