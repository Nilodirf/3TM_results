import numpy as np
from matplotlib import pyplot as plt
import os

def sixtyplot():
    temfile=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '60nmtem.txt'))
    f1file=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '60nmf1.txt'))
    f2file=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '60nmf2.txt'))
    f3file=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '60nmf3.txt'))

    tem=[float(i) for i in temfile.readlines()]
    f1=[float(i) for i in f1file.readlines()]
    f2=[float(i) for i in f2file.readlines()]
    f3=[float(i) for i in f3file.readlines()]

    plt.plot(tem, f1)
    plt.plot(tem, f2)
    plt.plot(tem, f3)

def tenplot():
    dat=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '5.6.txt'))
    vals=dat.readlines()
    x=np.array([float(i.split()[0]) for i in vals[2:]])
    y=np.array([float(line.split()[1]) for line in vals[2:]])
    plt.plot(x,y)

sixtyplot()
tenplot()
plt.xlim(1e-1, 1000)
plt.xscale('log')
plt.show()