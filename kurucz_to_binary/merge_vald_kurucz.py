import numpy as np

wvlm = 208.0

print('read 1')

#wvv, nuv, gfv, elv, x, euv, x, rav, stv, wav, x = np.loadtxt('vald_in_kurucz_format.dat',                unpack = True)

print('read 2')

#wvk, nuk, gfk, elk, x, euk, x, rak, stk, wak, x = np.loadtxt('Kurucz_comb_air_8.97670nm_to_10000nm.dat', unpack = True)

#xxv = np.zeros(len(wvv))
#xxk = np.zeros(len(wvk))

print('cut 1')

#wvv_cut = wvv[np.where(wvv <= wvlm)]
#nuv_cut = nuv[np.where(wvv <= wvlm)]
#gfv_cut = gfv[np.where(wvv <= wvlm)]
#elv_cut = elv[np.where(wvv <= wvlm)]
#xxv_cut = xxv[np.where(wvv <= wvlm)]
#euv_cut = euv[np.where(wvv <= wvlm)]
#rav_cut = rav[np.where(wvv <= wvlm)]
#stv_cut = stv[np.where(wvv <= wvlm)]
#wav_cut = wav[np.where(wvv <= wvlm)]

print('cut 2')

#wvk_cut = wvk[np.where(wvk > wvlm)]
#nuk_cut = nuk[np.where(wvk > wvlm)]
#gfk_cut = gfk[np.where(wvk > wvlm)]
#elk_cut = elk[np.where(wvk > wvlm)]
#xxk_cut = xxk[np.where(wvk > wvlm)]
#euk_cut = euk[np.where(wvk > wvlm)]
#rak_cut = rak[np.where(wvk > wvlm)]
#stk_cut = stk[np.where(wvk > wvlm)]
#wak_cut = wak[np.where(wvk > wvlm)]

print('merge')

#wvm = np.concatenate((wvv_cut, wvk_cut))
#num = np.concatenate((nuv_cut, nuk_cut))
#gfm = np.concatenate((gfv_cut, gfk_cut))
#elm = np.concatenate((elv_cut, elk_cut))
#xxm = np.concatenate((xxv_cut, xxk_cut))
#eum = np.concatenate((euv_cut, euk_cut))
#ram = np.concatenate((rav_cut, rak_cut))
#stm = np.concatenate((stv_cut, stk_cut))
#wam = np.concatenate((wav_cut, wak_cut))

print('save 1')

#np.savez('merge', wvm = wvm,\
#                  num = num,\
#                  gfm = gfm,\
#                  elm = elm,\
#                  xxm = xxm,\
#                  eum = eum,\
#                  ram = ram,\
#                  stm = stm,\
#                  wam = wam,)

print('load')

l = np.load('merge.npz')

wvm = l['wvm']
num = l['num']
gfm = l['gfm']
elm = l['elm']
xxm = l['xxm']
eum = l['eum']
ram = l['ram']
stm = l['stm']
wam = l['wam']

print('save 2')

frmt = ('%10.4f', '%5.2f', '%7.3f',) + 2 * ('%11.3f', '%5.1f',) + 3 * ('%5.2f',) + ('%i',)

np.savetxt('vald_kurucz_merged.dat', \
           np.column_stack([wvm, num, gfm, elm, xxm, eum, xxm, ram, stm, wam, xxm.astype(int)]), \
           fmt = frmt, delimiter = '   ')#, \
#           delimiter = '  ')
