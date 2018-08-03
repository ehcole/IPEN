import h5py
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/ss/IPEN-022/IPEN-022-1.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/ss/IPEN-022/IPEN-022-2.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")

f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/ss/IPEN-022/IPEN-022-3.h5", 'r')
keff = f["STATE_0001"]["keff"][()]
print((keff - 1) * 10**5, "pcm")
