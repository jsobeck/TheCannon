import pyfits
import os
import numpy as np

hdulist = pyfits.open("allStar-v603.fits")
datain = hdulist[1].data
apstarid= datain['APSTAR_ID']
for i in range(0, len(apstarid)):
    apstarid[i] = apstarid[i].split('.')[-1]

t = datain['TEFF']
g = datain['LOGG']
f = datain['FE_H']
params = datain['PARAM']
a = params[:,-1]

# read the real list of test stars
ts_lamost = np.loadtxt("../example_LAMOST/Test_Data.txt", dtype=str)
lamost_sorted = np.loadtxt('../example_LAMOST/lamost_sorted_by_ra.txt', 
        dtype=str)
apogee_sorted = np.loadtxt('apogee_sorted_by_ra.txt', dtype=str)

# find the apogee equivalents of the ts_lamost stars
# inds...these are the indices, in lamost_sorted, of all the training stars
# and thus these are the indices in apogee_sorted of all the training stars

inds = []
for star in ts_lamost:
    inds.append(np.where(lamost_sorted==star)[0][0])
inds = np.array(inds)
ts_apogee = apogee_sorted[inds]

# find the indices of the apogee training stars in the apstarid list

inds = []
for star in ts_apogee:
    ID = star.split('v603-')[1]
    ID = ID.split('.fits')[0]
    inds.append(np.where(apstarid==ID)[0][0])

inds = np.array(inds)

# now find the corresponding training values...
# this is in the order in which they appear in ts_apogee and ts_lamost

ids = apstarid[inds]
teff = t[inds]
logg = g[inds]
feh = f[inds]
alpha = a[inds]

# and now write the training file

nstars = len(teff)

file_out = open("apogee_test_labels.csv", "w")

header = 'id,teff,logg,feh,alpha\n'

file_out.write(header)

for i in range(nstars):
    print(i)
    line = str(ts_lamost[i])+','+str(teff[i])+','+str(logg[i])+','+str(feh[i])+','+str(alpha[i])+'\n'
    file_out.write(line)

file_out.flush()
file_out.close()