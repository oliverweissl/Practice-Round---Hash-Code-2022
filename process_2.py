import glob
import numpy as np

def happy_check(INGR, CST:int, likes, dislikes):
    happy_cst = 0
    for cst in range(CST):
        happy_cst = happy_cst + 1 if set(likes[cst]).issubset(INGR) and not(set(dislikes[cst]).issubset(INGR)) else happy_cst - 1
    return happy_cst


def process(file:str):
    with open(file,"r") as fl:
        data = fl.readlines()
        pass
    NAME = file.split(".")[0]
    AMT = int(data[0])

    dat = data[-(AMT * 2):]
    l1 = dat[::2]
    l2 = dat[1::2]

    for i in range(AMT):
        l1[i] = l1[i].replace("\n","").split(" ")[-int(l1[i][0]):]
        l2[i] = l2[i].replace("\n","").split(" ")[-int(l2[i][0]):]

        if l1[i][0].isnumeric(): l1[i].pop(0)
        if l2[i][0].isnumeric(): l2[i].pop(0)

    flat_l1 = sum(l1, [])
    flat_l2 = sum(l2, [])

    d_d = set(flat_l2)
    l = set(flat_l1)

    INGR = d_d.union(l)

    l1np = np.array(l1)
    l2np = np.array(l2)

    temp_d_d = d_d
    min_rat = happy_check(INGR,AMT,l1np,l2np)
    for i in range(len(d_d)):
        perf = []
        for ingr in temp_d_d:
            temp_ing = INGR
            temp_ing.remove(ingr)
            ratio = happy_check(temp_ing,AMT,l1np,l2np)
            temp_ing.add(ingr)
            perf.append((ratio,ingr))

        perf.sort(reverse=True)
        if perf[0][0] >= min_rat:
            INGR.remove(perf[0][1])
            temp_d_d.remove(perf[0][1])
            min_rat = perf[0][0]

    with open(f"{NAME}.out.txt", "w") as file:
        file.write(f'{len(INGR)} {" ".join(INGR)}')
        pass


myFiles = glob.glob('*.in.txt')
#myFiles = "a_an_example.in.txt"
#process(myFiles)
for file in myFiles:
    process(file)
