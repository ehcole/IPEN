import h5py
import numpy as np
import sys

#TODO: replace with path to h5 files. p should be 2D cases with control rods out and f with rods in, both with fine mesh
for i in range(1, 4):
    p = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/boron/IPEN-020/4-2-" + str(i) + ".h5", 'r')
    f = h5py.File("/scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version4/boron/IPEN-019/4-2-" + str(i) + ".h5", 'r')
    expData = np.array([2438.05, 2311.40, 2195.85, 1975.38, 1449.33, 222.16])
    results = np.zeros(expData.shape)
    boronConc = np.array([0.082, 6.067, 11.028, 21.98, 43.23, 95.742])
    delta = np.zeros(len(boronConc) - 1)
    keffs = np.zeros(6)
    keffps = np.zeros(6)
    for i in range(1, 7):
        state = "STATE_000" + str(i)
        keff = f[state]['keff'][()]
        keffp = p[state]['keff'][()]
        results[i - 1] = abs(keffp - keff) / (keffp * keff) * 10**5
        keffs[i - 1] = keff * 10**5
        keffps[i - 1] = keffp * 10**5
    print(results.mean())
    diffs = results - expData
    absDiffs = np.absolute(diffs)
    diffPercents = absDiffs / expData
    print("Individual case MAPE:", diffPercents[:-1].mean())


    
    for i in range(1, len(boronConc)):
        delta[i - 1] = (keffps[i] - keffps[i - 1]) / (boronConc[i] - boronConc[i - 1])
    print("Boron reactivity coefficient:", delta.mean())
    print("Percent error:", abs((delta.mean() + 23.25) / 23.25))
