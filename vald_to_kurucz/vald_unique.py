import pandas as pd
import numpy as np

import sys

if not '/mnt/SSD/sim/python/src/aux/' in sys.path:

    sys.path.append('/mnt/SSD/sim/python/src/aux/')

import importlib

import phys; importlib.reload(phys)
import auxfunc; importlib.reload(auxfunc)

from tqdm import tqdm

#df = pd.read_csv('vald_short.dat')
df = pd.read_csv('vald.dat')

ei = df.iloc[:, 0].tolist()

eleion = []

wvl = []
E = []
gf = []
rad = []
stark = []
waals = []

for i in tqdm(range(len(df)), ncols = auxfunc.term_width(), desc = 'Converting'):

    d = ei[i].replace("'", "")

    key = d.split()[0]

    if key == 'Y': continue

    ele = phys.ptable[key]['atnum']

    ion = int(d.split()[1]) - 1

    eleion.append(ele + 0.01 * ion)

    wvl.append(df.iloc[i, 1])
    E.append(df.iloc[i, 2])
    gf.append(df.iloc[i, 3])
    rad.append(df.iloc[i, 4])
    stark.append(df.iloc[i, 5])
    waals.append(df.iloc[i, 6])

eleion = np.array(eleion)
wvl = np.array(wvl)
E = np.array(E)
gf = np.array(gf)
rad = np.array(rad)
stark = np.array(stark)
waals = np.array(waals)

idx = np.unique(wvl, return_index = True)[1]

eleion = eleion[idx]
wvl = wvl[idx]
E = E[idx]
gf = gf[idx]
rad = rad[idx]
stark = stark[idx]
waals = waals[idx]

np.savetxt('vald_unique.dat', np.transpose((eleion, wvl, E, gf, rad, stark, waals)), \
fmt = ('%5.2f', '%9.3f', '%6.3f', '%7.3f', '%6.3f', '%6.3f', '%6.3f'), delimiter = '         ')
