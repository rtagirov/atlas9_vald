import pandas as pd
import numpy as np

import importlib

#import phys; importlib.reload(phys)

from tqdm import tqdm

v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11 = np.loadtxt('Kurucz_comb_air_8.97670nm_to_10000nm.dat.overlap', unpack = True)

wvl = 1.0e+7 / (v6 - v4)

idx1 = np.unique(wvl, return_index = True)[1]

v1 =  v1[idx1]
v2 =  v2[idx1]
v3 =  v3[idx1]
v4 =  v4[idx1]
v5 =  v5[idx1]
v6 =  v6[idx1]
v7 =  v7[idx1]
v8 =  v8[idx1]
v9 =  v9[idx1]
v10 = v10[idx1]
v11 = v11[idx1]

idx2 = np.argsort(v1)

v1 =  v1[idx2]
v2 =  v2[idx2]
v3 =  v3[idx2]
v4 =  v4[idx2]
v5 =  v5[idx2]
v6 =  v6[idx2]
v7 =  v7[idx2]
v8 =  v8[idx2]
v9 =  v9[idx2]
v10 = v10[idx2]
v11 = v11[idx2]

np.savetxt('Kurucz_comb_air_8.97670nm_to_10000nm.dat', np.transpose((v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11)), \
fmt = ('%10.4f', '%5.2f', '%7.3f', '%11.3f', '%5.1f', '%11.3f', '%5.1f', '%5.2f', '%5.2f', '%5.2f', '%1i'), delimiter = '   ')
#form2 = '(F10.4,1X,
#          F5.2,1X,
#          F7.3,2X, 
#          F11.3, 
#          F5.1, 2X, 
#          F11.3,
#          F5.1,3X,
#          F5.2,2X,
#          F5.2,2X,
#          F5.2,1X,
#          I1)'
