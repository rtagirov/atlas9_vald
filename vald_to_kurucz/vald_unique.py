import pandas as pd
import numpy as np

import importlib

import phys; importlib.reload(phys)

from tqdm import tqdm

lines_seen = set() # holds lines already seen

outfile = open('vald_unique.dat', "w")

for line in open('vald.dat', "r"):

    if line not in lines_seen: # not a duplicate

        outfile.write(line)

        lines_seen.add(line)

outfile.close()

df = pd.read_csv('vald_unique.dat', low_memory = False)

ei = df.iloc[:, 0].tolist()

eleion = []

wvl = []
E = []
gf = []
rad = []
stark = []
waals = []

for i in tqdm(range(len(df)), desc = 'Converting'):

    d = ei[i].replace("'", "")

    key = d.split()[0]

#    if key == 'Y': continue

    ele = phys.ptable[key]['atnum']

    ion = int(d.split()[1]) - 1

    eleion.append(ele + 0.01 * ion)

    wvl.append(df.iloc[i, 1])
    E.append(df.iloc[i, 2])
    gf.append(df.iloc[i, 3])
    rad.append(df.iloc[i, 4])
    stark.append(df.iloc[i, 5])

#    if len(df.iloc[i, 6]) <= 6:

#        waals.append(np.float32(df.iloc[i, 6]))

#    else:

    waals.append(np.float32(df.iloc[i, 6][:6]))
#    waals.append(np.float32(df.iloc[i, 6].replace("'", "").replace(")Cu", "").replace(" 52 CDROM18              H", "").replace("C+", "").replace("(65", "")))

eleion = np.array(eleion)
wvl = np.array(wvl)
E = np.array(E)
gf = np.array(gf)
rad = np.array(rad)
stark = np.array(stark)
waals = np.array(waals)

#idx = np.unique(wvl, return_index = True)[1]

#eleion = eleion[idx]
#wvl = wvl[idx]
#E = E[idx]
#gf = gf[idx]
#rad = rad[idx]
#stark = stark[idx]
#waals = waals[idx]

np.savetxt('vald_unique_first_column_converted.dat', np.transpose((eleion, wvl, E, gf, rad, stark, waals)), \
fmt = ('%5.2f', '%9.3f', '%6.3f', '%7.3f', '%6.3f', '%6.3f', '%6.3f'), delimiter = '         ')
