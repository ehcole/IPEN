import h5py
import numpy as np
#TO DO: define path to top level git directory
pathToTopLevel = '.'
#f0 is the case with no plates (-7.h5)
f0 = h5py.File(pathToTopLevel + "/experiments/4.3/outputs/4-3_carbon/4-3-7.h5", 'r')
expData = np.array([154.91, 111.68, -4.14, -67.01, -249.83, -348.68, -344.79])
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
