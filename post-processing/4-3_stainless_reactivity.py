import h5py
import numpy as np
#TODO: define path to top level git dir
pathToTopLevel = '.'
#f0 should be the case with all plates removed (-7.h5)
f0 = h5py.File(pathToTopLevel + "/experiments/4.3/outputs/4-3_stainless/4-3-7.h5", 'r')
expData = np.array([160.41, 117.18, 1.36, -61.51, -244.33, -343.18, -339.29])
#expData = np.array([154.91, 111.68, -4.14, -138.47, -249.83, -348.68, -344.79])
results = np.zeros(expData.shape[0])
keff0 = f0["STATE_0001/keff"][()]
for i in range(1, 8):
    try:
        f = h5py.File(pathToTopLevel + "/experiments/4.3/outputs/4-3_carbon/4-3-" + str(i) + ".h5", 'r')
    except:
        exit(0)
    else:
        try:
            keff1 = f["STATE_0001/keff"][()]
        except:
            exit(0)
        else:
            numPlates = 32 - i * 5
            if numPlates < 0:
                numPlates = 0
    if i != 7:
        results[i] = (keff1 - keff0) * 10**5 / (keff1 * keff0)
print(results)
print(expData)
diffs = results - expData
absDiffs = np.absolute(diffs)
print(absDiffs.mean())
diffsPercents = absDiffs / results
absDiffsPercents = np.absolute(diffsPercents)
print(absDiffsPercents.mean())
