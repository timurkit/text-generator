import sys
import random
def ara_ara():
    L=int(input())
    txt = sys.stdin.read().replace("\n    ", " @ ").split()
    trios=set()
    for i in range(len(txt)-3):
        trios.add((txt[i],txt[i+1],txt[i+2],txt[i+3]))
    

    word_dict={}
    for w1,w2,w3,w4 in trios:
        if (w1,w2) in word_dict.keys():
            word_dict[(w1,w2)].add((w3,w4))
        else:
            word_dict[(w1,w2)] = set()
            word_dict[(w1,w2)].add((w3,w4))

    seq=range(len(txt)//2)
    count=random.choice(seq)
    fw=(txt[count],txt[1+count])
    while fw[0].islower():
        count=random.choice(seq)
        fw=(txt[count],txt[1+count])

    chain=[fw]    
    nw=L
    k=-1
    for i in range(nw//2):
        chain.append(random.choice(list(word_dict[chain[-1]])))

    res=[item for t in chain for item in t]
    res=' '.join(res[:L]).replace("@","\n    ")
    print(res)    

if __name__ == '__main__':
    ara_ara()
