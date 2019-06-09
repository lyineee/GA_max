import numpy as np 
import random

def get_gene():
    #divide 100 for float
    geneList=[]
    for i in range(100):
        geneList.append(random.randrange(0,1500,1)/100)
    # return geneList
    return np.array(geneList)

def cal_mean(geneList):
    result=(-3)*(geneList-30)**2*np.sin(geneList)
    '''
    print(result)
    mean=result/np.sum(result)
    print(mean)
    resultList=np.array()
    for index in range(len(result)):
        if mean[index]>=random.random():
            resultList=np.append(resultList,geneList[index])
    return resultList
    '''
    mean=result/np.sum(result)
    


def random_from_gene(geneList,kList):
    pass 

if __name__ == "__main__":
    print(cal_mean(get_gene()))
