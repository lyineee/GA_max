import numpy as np 
import random

def get_gene():
    #divide 100 for float
    geneList=[]
    for i in range(100):
        geneList.append(gen_bin())
    # return geneList
    return np.array(geneList)

def gen_bin():
    gen=''
    for i in range(16):
        gen+=str(random.randrange(0,2))
    return gen
    


def cal_mean(geneList):
    #TODO add end condition
    result=(-3)*(gen_list_decode(geneList)-30)**2*np.sin(gen_list_decode(geneList))
    #make result greater than 0
    result+=3000
    mean=result/np.sum(result)
    nextGen=[]

    for i,j in choice_two_from_gene(mean,50):
        nextGen+=gene_crossover(geneList[i],geneList[j])
    nextGen=np.array(nextGen)
    return [nextGen,mean]

def gene_variation(geneList,klist):
    n=30
    # geneList=list(geneListA)
    for i in range(n):
        num=choice_one_from_gene(klist)
        gene=list(geneList[num])
        gene[choice_one_from_gene([1/16]*16)]=str(random.randint(0,1))
        geneList[num]=''.join(gene)

    return geneList
        
def gene_crossover(gen1,gen2):
    crossPoint=random.randint(0,15)
    gen1p=[gen1[0:crossPoint],gen1[crossPoint:]]
    gen2p=[gen2[0:crossPoint],gen2[crossPoint:]]
    ngen1=gen1p[0]+gen2p[1]
    ngen2=gen2p[0]+gen1p[1]
    return [ngen1,ngen2]




    
def choice_one_from_gene(kList):
        k=0
        randnum=random.random()
        for i in range(len(kList)):
            if k<=randnum<=k+kList[i]:
                return i
            k+=kList[i]

def choice_two_from_gene(kList,num):
    for j in range(num):
        yield [choice_one_from_gene(kList),choice_one_from_gene(kList)]

    
def gen_decode(gen):

    data=str(int(gen[:3],2))+'.'+str(int(gen[2:],2))
    data=float(data)
    return data

def gen_list_decode(genList):
    data=[]
    for i in range(genList.size):
        data.append(gen_decode(genList[i]))
    data=np.array(data)
    return data
    
def iteration():
    gene=get_gene()
    for i in range(50):
        a,klist=cal_mean(gene)
        gene=gene_variation(a,klist)
    result=gen_list_decode(gene)
    print(result)
    print(np.mean(result))



        

def test():
    a=cal_mean(get_gene())
    print(a)
    #print(gen_decode(a))
    # print(len(a))




if __name__ == "__main__":
    iteration()
