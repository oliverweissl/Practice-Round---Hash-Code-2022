import glob

def process(file:str):
    NAME = file.split(".")[0]
    with open(file) as file:
        data = file.readlines()
        pass

    AMT = int(data[0])
    dat = data[-(AMT*2):]

    l1 = dat[::2]
    l2 = dat[1::2]

    for i in range(AMT):
        l1[i] = l1[i].replace("\n","").split(" ")[-int(l1[i][0]):]
        l2[i] = l2[i].replace("\n","").split(" ")[-int(l2[i][0]):]

        if l1[i][0].isnumeric(): l1[i].pop(0)
        if l2[i][0].isnumeric(): l2[i].pop(0)

    f1 = set(sum(l1, []))
    f2 = set(sum(l2, []))

    final = list(f1-f2)
    with open(f"{NAME}.out.txt", "w") as file:
        file.write(f'{len(final)} {" ".join(final)}')
        pass

myFiles = glob.glob('*.in.txt')
for file in myFiles:
    process(file)
