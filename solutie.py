# load a tetwork
import os
from random import seed
from random import randint
from copy import deepcopy
from random import random
seed(5)
def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


def incrucisare(parent1,parent2,network):
    c1 = []
    geneA = randint(0, network['noNodes'] - 1)
    geneB = randint(0, network['noNodes'] - 1)
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        c1.append(parent1[i])
    c2 = [item for item in parent2 if item not in c1]
    child = c1 + c2
    return child
def mutate(community,network):
    gena1=randint(0,network["noNodes"]-1)
    gena2= randint(0, network["noNodes"] - 1)
    aux=community[gena1]
    community[gena1]=community[gena2]
    community[gena2]=aux
    return community
def calcFitness(param, network):
    s=0
    for i in range(0,len(param)-1):
        if network["mat"][param[i]][param[i+1]]==0:
            s=int("infinity")
        else:
            s+=network["mat"][param[i]][param[i+1]]
    if network["mat"][param[0]][param[-1]]==0:
        s=int("infinity")
    else:
        s+=network["mat"][param[0]][param[-1]]
    return s
network=readNet("fisierIn.in")
population=[]
n=50
for j in range (0,n):
    population.append([])
    while len(population[j])<network["noNodes"]:
        elem=randint(0,network["noNodes"]-1)
        if elem not in population[j]:
            population[j].append(elem)
for j in range(0,500):
    fitness=[]
    for i in range(0,n):
        fitness.append(calcFitness(population[i],network))
    popNoua = []
    visited=[0]*n
    value=[0]*n
    for i in range(0,n):
        prob=randint(1,5)
        value[i]=prob*(fitness[i])
    sortat2=sorted(range(0,n),key=lambda x:value[x])
    sortat=sorted(range(0,n),key=lambda x:fitness[x])
    print(calcFitness(population[sortat[0]],network))
    i=0
    copil=incrucisare(population[sortat2[0]],population[sortat2[1]],network)
    p=randint(1,10)
    if(p<3):
        mutant=mutate(copil,network)
    else:
        mutant=copil
    population.remove(population[sortat[-1]])
    population.append(mutant)
file=open("adjnoun.out","w")
print(population[sortat[0]])

