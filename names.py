#!/usr/bin/python3

import os
import matplotlib.pyplot as plt

boys={}
girls= {}

def readone(yr):
    fn = "yob"+str(yr)+".txt"
    dn = "baby/"
    path=dn+fn
    gd={}
    girls[yr]=gd
    bd={}
    boys[yr]=bd
#    print(dn,fn,path)
    with open(path,"r") as f:
        for l in f:
            l.strip()
            tks=l.split(",")
            if tks[1]=="F":
                gd[tks[0]]=int(tks[2])
            else:
                bd[tks[0]]=int(tks[2])

def listone(dc,yrs,yre,nm):
	rv=[]
	for yr in range(yrs,yre+1):
		dictxxx = dc[yr]
		if nm in dictxxx:
			rv.append(dictxxx[nm])
		else:
			rv.append(0)
	return rv                      

for bob in range(1882,2015):
    readone(bob)

nm_morris=listone(boys,1882,2014,"Sam")

plt.plot([x for x in range(1882,2015)],nm_morris)
plt.show()











