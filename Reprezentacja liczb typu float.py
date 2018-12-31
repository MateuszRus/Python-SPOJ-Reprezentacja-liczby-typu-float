def sign(f):
    if(f < 0) :
        return 1
    else:
        return 0

def convertToBin(res, dec):
    for x in range(8):
        whole, dec = str((float(decimal_converter(dec))) * 2).split(".")

        dec = int(dec)

        res += whole

    return res

def exponent(whole, n):
    if(whole != 0.0):
        return str(bin(n + 127).lstrip("0b"))
    else:
        return "00000000"


def mantissa(number):
    whole, dec = str(float(number)).split(".")

    whole = int(whole)
    dec = int(dec)

    if(whole < 0):
        whole = whole * -1

    res = str(bin(whole).lstrip("0b"))

    exponentCount = str(len(res) - 1)

    res = res[1:]

    if(whole != 1.0):
        exponentCount = str(len(res))

    return exponent(whole, int(exponentCount)).rjust(8, '0') + convertToBin(res, dec).ljust(23, '0')

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

def changeToHex(res):
    ret = ""

    if(res < 10):
        ret = str(res)
    if (res == 10):
        ret = 'a'
    if(res == 11):
        ret = 'b'
    if (res == 12):
        ret = 'c'
    if(res == 13):
        ret = 'd'
    if (res == 14):
        ret = 'e'
    if(res == 15):
        ret = 'f'

    return ret

def binaryToHex(line):
    tab = [line[i:i + 4] for i in range(0, len(line), 4)]
    tables = ""

    for i in tab:
        res = 0;
        tableRes = i[::-1]

        for j in range(0, 4):
            res += int(tableRes[j]) * 2**int(j)

        tables += changeToHex(res)


    ret = ""
    tempTab = [str(tables)[i:i + 2] for i in range(0, len(str(tables)), 2)]
    for j in tempTab:
        if(j == "00"):
            ret += "0 "
        else:
            ret +=  j + " "

    return ret[:-1]

def printfloat(f):
    line = str(sign(f)) + str(mantissa(f))

    print(binaryToHex(line))


numberOfAttempts = input()
returns = []

for x in range(0, int(numberOfAttempts)):
    numer = input()

    returns.append(printfloat(float(numer)))

