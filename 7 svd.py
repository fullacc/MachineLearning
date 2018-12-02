import numpy as np
import pandas as pd
from math import sqrt
import scipy
from scipy import linalg
def SVD(A):
    print(A)
    AT = A.transpose()
    AdotAT = A.dot(AT)
    ATdotA = AT.dot(A)            
    a, V = linalg.eig(ATdotA)
    print(a)
    VT = V.transpose()
    for i in range(len(a)):
        a[i] = sqrt(abs(a[i]))
    a = sorted(a, reverse = True)
    S = np.diag(a)
    S_inversed = np.linalg.inv(S
    for i in range(len(V)):
        print(V[:,i])
    U = A.dot(V.dot(S_inversed))    
    u, s, v = np.linalg.svd(A)
    print("-------------")
    print(U)
    print(S)
    print(V)
    print("-------------")
    print(u)
    print(s)
    print(v)          
    print("-------------")
    print(A)
    print(U.dot(S.dot(VT)))
    return 0


A = np.array([[0, 1, 1], [sqrt(2), 2, 0], [0, 1, 1]])
SVD(A)