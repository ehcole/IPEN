import os
print("low buckling")
os.system("python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/temp/IPEN-028b/IPEN-028-1.h5")
print("med buckling (nominal)")
os.system("python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/temp/IPEN-028b/IPEN-028-2.h5")
print("high buckling")
os.system("python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/k_eff.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/temp/IPEN-028b/IPEN-028-3.h5")
