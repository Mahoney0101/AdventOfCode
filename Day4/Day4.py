import numpy as np

def get_data():
    file_name = f"Day4/input.txt"

    with open(file_name) as fp:
        data = fp.read().strip().split('Split data')
        data = [d.strip().split("\n") for d in data]
        return data

testData,challengeData = get_data()

def get_blocks(dt):
    block = []
    num = [int(i) for i in dt[0].split(",")]
    row = []
    tdata=[]
    blocks = 0
    for d in dt[2:]:
        if d == "":
            tdata.append(block)
            block=[]
            blocks+=1
        else:
            block.append([int(i) for i in d.strip().split(" ") if i!=""])
    tdata.append(block)
    block=[]
    blocks+=1
    tdata = np.array(tdata).reshape(blocks,-1, 5)
    return tdata, num

def first_matched(tdata, num):
    results = np.zeros_like(tdata).astype(bool)
    matched = False

    for n in num:
        for i,block in enumerate(tdata):
            results[i] += block==n
            if (results[i]==[ True,  True,  True,  True,  True]).all(axis=1).any():
                matched=True
                break
            if (results[i].T==[ True,  True,  True,  True,  True]).all(axis=1).any():
                matched=True
                break
        if matched:
            s = (tdata[i]*~results[i]).sum()
            print(f"Answer: {n*s}\n")
            break

def last_matched(tdata, num):
    results = np.zeros_like(tdata).astype(bool)
    matched = False
    mblocks=[]
    all_blocks = list(range(0, len(results)))

    for n in num:
        for i,block in enumerate(tdata):
            results[i] += block==n
            if (results[i]==[ True,  True,  True,  True,  True]).all(axis=1).any():
                if i not in mblocks:
                    mblocks.append(i)
                if len(mblocks) == len(all_blocks):
                    matched=True
            if (results[i].T==[ True,  True,  True,  True,  True]).all(axis=1).any():
                if i not in mblocks:
                    mblocks.append(i)
                if len(mblocks) == len(all_blocks):
                    matched=True
        if matched:
            i = mblocks[i]
            s = (tdata[i]*~results[i]).sum()
            print(f"Answer: {n*s}")
            break

d1,n1 = get_blocks(challengeData)
first_matched(tdata=d1, num=n1)
last_matched(tdata=d1, num=n1)
