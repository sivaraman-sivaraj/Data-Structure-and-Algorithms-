import numpy as np, math
import matplotlib.pyplot as plt

def f(n):
    e1 = np.log(n)
    e2 = np.sqrt(n)
    e3 = n
    e4 = n*(np.log(n))
    e5 = n**2
    e6 = n**3
    e7 = 2**n
    e8 = math.factorial(n)
    return [e1,e2,e3,e4,e5,e6,e7,e8]

ss = [10,20,30,40,50,60,70,80,90,100]


def run(n):
    M = [list(),list(),list(),list(),
        list(),list(),list(),list()]
    for i in range(len(n)):
        temp = f(n[i])
        M[0].append(temp[0])
        M[1].append(temp[1])
        M[2].append(temp[2])
        M[3].append(temp[3])
        M[4].append(temp[4])
        M[5].append(temp[5])
        M[6].append(temp[6])
        M[7].append(temp[7])
    return M

M = run(ss)

print(M)


    
def plot(M):
    X = np.arange(len(M[0]))
    plt.figure()
    plt.plot(X,M[0],label = "log n")
    plt.plot(X,M[1],label = "sqrt n")
    plt.plot(X,M[2],label = "n ")
    plt.plot(X,M[3],label = "n log n ")
    #plt.plot(X,M[4],label = "n^2 ")
    #plt.plot(X,M[5],label = "n^3")
    #plt.plot(X,M[6],label = "2^n")
    #plt.plot(X,M[7],label = " n!")
    plt.xlabel("Number of function calls")
    plt.ylabel("Runtime Comparision")
    plt.legend(loc = "best")
    plt.show()

plot(M)