import numpy as np
def coeff(x):
    X = x[:,0]
    Y = x[:,1]
    
    if len(X)>=11:
        L = 10
    else:
        L = len(X)-1
        
    nm = np.zeros((L,1))
    
    for i in range(1,L):
        fit = np.polyfit(X,Y,i)
        val = np.polyval(fit,X)
        nm[i-1,0] = np.linalg.norm(Y-val)
        
    I = nm.argmin()
    coeff = np.polyfit(X,Y,I)

    print(coeff)