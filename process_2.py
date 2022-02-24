import glob
import numpy as np
import time
from collections import defaultdict

def happy_check(INGR):
    happy_cst = 0
    for cst in range(AMT):
        happy_cst = happy_cst + 1 if set(l1np[cst]).issubset(INGR) and not(set(l2np[cst]).issubset(INGR)) else happy_cst - 1
    return happy_cst

def make_tuple(ingr):
    try:
        INGR.remove(ingr)
        ratio = happy_check(INGR)
        INGR.add(ingr)
    except:
        ratio = -1000000
    return ratio,ingr

def process(file:str):
    with open(file,"r") as fl:
        data = fl.readlines()
        pass
    NAME = file.split(".")[0]
    print(f"\nstarting: {NAME}")

    global AMT
    AMT = int(data[0])

    dat = data[1:]
    l1 = dat[::2]
    l2 = dat[1::2]

    for i in range(AMT):
        l1[i] = l1[i].replace("\n","").split(" ")[-int(l1[i][0]):]
        l2[i] = l2[i].replace("\n","").split(" ")[-int(l2[i][0]):]

        if l1[i][0].isnumeric(): l1[i].pop(0)
        if l2[i][0].isnumeric(): l2[i].pop(0)


    d_d = set(sum(l2, []))
    amt_d = len(d_d)
    l = set(sum(l1, []))

    global INGR
    INGR = d_d.union(l)

    global l1np
    l1np = np.array(l1,dtype=object)
    global l2np
    l2np = np.array(l2,dtype=object)

    min_rat = happy_check(INGR)
    perf = list(map(make_tuple, d_d))
    lenp = len(perf)
    perf.sort(reverse=True)
    for i in range(lenp):
        x = time.perf_counter()
        min_v = perf[i][0]
        check = [y for (x, y) in perf[i:] if x == min_v]
        a_perf = list(map(make_tuple, check))
        a_perf.sort(reverse=True)
        if a_perf[0][0] >= min_rat:
            INGR.remove(a_perf[0][1])
            min_rat = a_perf[0][0]

        t = time.perf_counter()-x
        print(f"{len(perf)-i} iterations left | took: {t}sec")

    with open(f"{NAME}.out.txt", "w") as file:
        file.write(f'{len(INGR)} {" ".join(INGR)}')
        pass

myFiles = glob.glob('*.in.txt')
#myFiles = "e_elaborate.in.txt"
#process(myFiles)
for file in myFiles:
    process(file)
