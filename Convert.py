FROM_BASE = 16

def fromStr(fromStr):
    toInt = 0
    power = 1
    for i in range(len(fromStr) - 1, -1, -1):
#if FROM_BASE < 10:
        toInt = toInt + power * int(fromStr[i])
#else
        if fromStr[i].isdigit():
            toInt = toInt + power * int(fromStr[i])
        else:
            toInt = toInt + power * (ord(fromStr[i].upper()) - ord("A") + 10)
#endif
        power = power * FROM_BASE
    return toInt

TO_BASE = 16

def toStr(fromInt):
    toStr = ""
    while fromInt > 0:
        value = fromInt % TO_BASE
#if TO_BASE < 10:
        toStr = str(value) + toStr
#else
        if value < 10:
            toStr = str(value) + toStr
        else:
            toStr = chr(value - 10 + ord("A")) + toStr
#endif
        fromInt = fromInt // TO_BASE
    return toStr
