function vaclambda, airlambda

; translate airlambda to the vacuum
; Wavelengths should be in A

lambda = airlambda / 10. ; A to nm

sqwave = (1.0E+07 / lambda)^2.

increase = 1.0000834213E+00 +2.406030E+06/(1.30E+10 - sqwave) + 1.5997E+04/(3.89E+09 - sqwave)

return, increase * airlambda

end

pro convert

openr, lun1, 'vald_unique.dat',           /get_lun
openw, lun2, 'vald_in_kurucz_format.dat', /get_lun

;mendeleev = ['H ','He','Li','Be','B ','C ','N ','O ','F ','Ne','Na','Mg','Al','Si', $
;             'P ','S ','Cl','Ar','K ','Ca','Sc','Ti','V ','Cr','Mn','Fe','Co','Ni','Cu','Zn']

evtocm = 8065.5447

Nlines = file_lines('vald_unique.dat')

;des = '      '

i = 0.

;form1 = '(A6, 8X, F9.4,3X, F7.4,1x,F7.3,2x,F5.3,1x,f6.3,1x,f6.3)'

;form2 = '(F10.4,1X,F5.2,1X,F7.3,2X, F11.3, F5.1, 2X, F11.3,F5.1,3X,F4.2,2X,F5.2,2X,F5.2,1X,I1)'
form2 = '(F10.4,1X,F5.2,1X,F7.3,2X, F11.3, F5.1, 2X, F11.3,F5.1,3X,F5.2,2X,F5.2,2X,F5.2,1X,I1)'

while (i le Nlines - 1) do begin

       print, 'Processing ', i

;       readf, lun1, FORMAT = form1, des, wavh, exch, gfh, radh, starkh, waalsh
       readf, lun1, kurnum, wavh, exch, gfh, radh, starkh, waalsh

;       num = where(mendeleev eq strmid(des, 1, 2)) + 1

;       ion = string(strmid(des, 4, 1), format = '(i1)') - 1.

;       kurnum = num + 0.01 * ion

       if (wavh le 2000.) then wav = wavh

       if (wavh gt 2000.) then wav = vaclambda(wavh)

       Eup = exch * evtocm + 1.d8 / wav

       if (gfh gt -16.3) then begin

            printf, lun2, FORMAT = form2, wav / 10., kurnum, gfh, exch * evtocm, 0., Eup, 0., radh, starkh, waalsh, 0

       endif
 
       i = i + 1.

endwhile

free_lun, lun1
free_lun, lun2

end
