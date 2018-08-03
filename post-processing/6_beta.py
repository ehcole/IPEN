import h5py
import numpy as np
import sys
import os

#TODO: Replace with to h5 file
f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-008/6.h5", 'r')
beta = f["STATE_0002/beta"][()]
genTime = f["STATE_0002/generation_time"][()] * 10**6
print("Beta Effective:", beta * 10**5)
print("Error:", beta * 10**5 - 779.85, "pcm")
print("Lambda:", genTime)
print("Percent Error:", abs(genTime - 29.73) / 29.73)
