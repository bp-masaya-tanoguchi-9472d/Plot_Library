import matplotlib.pyplot as plt
import numpy as np
from matplotlib_venn import venn3

def venn(X,Y,Z,set_labels):
    x = np.unique(X)
    y = np.unique(Y)
    z = np.unique(Z)

    all_and = list(set(x)&set(y)&set(z))

    x_or_com = list(set(x)^set(all_and))
    y_or_com = list(set(y)^set(all_and))
    z_or_com = list(set(z)^set(all_and))

    xy_and = list(set(x_or_com) & set(y_or_com))
    yz_and = list(set(y_or_com) & set(z_or_com))
    zx_and = list(set(z_or_com) & set(x_or_com))
    
    x_or = list(set(x) ^ set(np.append(np.append(xy_and,zx_and),all_and)))#x
    y_or = list(set(y) ^ set(np.append(np.append(xy_and,yz_and),all_and)))#y
    z_or = list(set(z) ^ set(np.append(np.append(yz_and,zx_and),all_and)))#z
    
    subsets = (len(x_or),len(y_or),len(xy_and),len(z_or),len(yz_and),len(zx_and),len(all_and))

    print(set_labels)
    
    plt.figure()
    venn3(subsets=subsets, set_labels=set_labels)
    plt.show()
