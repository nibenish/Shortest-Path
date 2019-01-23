def main():
    with open("input.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line.strip('\n'))
    nodes = makeNodes(array)
    makeList(nodes)

def makeNodes(arrayIn):
    arrayOut = []
    for ent in arrayIn:
        data = ent.split(":")
        arrayOut.append(data)
    return arrayOut

def makeList(A):
    strout = ""
    while A != []:
        cond = True
        for x in A:
            if x[1] == '':
                strout+=(x[0] + " ")
                A.remove(x)
            else:
                names = x[1].split(' ')
                for y in names:
                    if y not in strout:
                        cond = False
                if cond:
                    strout+=(x[0] + " ")
                    A.remove(x)
    print(strout)

main()
