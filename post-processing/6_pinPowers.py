from __future__ import division
import numpy as np
import h5py
import sys


'''this code analyzes pin power data from the IPEN experiments. it is designed to be run for either a 2D or 3D
model of a core with one assembly. Takes h5 file as argument.'''
#TODO: define path to top level git dir
pathToTopLevel = '.'
#load data
expData = np.genfromtxt(pathToTopLevel + "/post-processing/experimental_data/pinPowers.csv", delimiter=',')
h5 = h5py.File(sys.argv[1], 'r')
modelData4D = h5["STATE_0001/pin_powers"]
modelData = np.zeros([modelData4D.shape[0], modelData4D.shape[1]])

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

#populate 2D array of model data, axially integrate pin power
#note: simple average was used here because the planar levels of the fuel cells
#were evenly distributed
for i in range(modelData.shape[0]):
    for j in range(modelData.shape[1]):
        for k in range(modelData4D.shape[2]):
            modelData[i][j] += modelData4D[i][j][k][0] / modelData4D.shape[2]

#normalize experimental data
numNonzeros = 0
total = 0
for i in range(expData.shape[0]):
    for j in range(expData.shape[1]):
        if expData[i][j]:
            numNonzeros += 1
            total += expData[i][j]
expDataMean = total / numNonzeros
normalizedExpData = expData / expDataMean


#diffPercents is percent error ((model datapoint - exp datapoint) / exp datapoint)
diffs = np.zeros(expData.shape)
diffPercents = np.zeros(expData.shape)
numDatapoints = 0
expDataList = list()
modelDataList = list()

for i in range(normalizedExpData.shape[0]):
    for j in range(normalizedExpData.shape[1]):
        if normalizedExpData[i][j] and modelData[i][j]:
            numDatapoints += 1
            diffs[i][j] = normalizedExpData[i][j] - modelData[i][j]
            diffPercents[i][j] = diffs[i][j] / normalizedExpData[i][j]
            expDataList.append(normalizedExpData[i][j])
            modelDataList.append(modelData[i][j])


expDatapoints = np.array(expDataList)
modelDatapoints = np.array(modelDataList)
absPercents = np.absolute(diffPercents)

print("MAPE:", np.mean(absPercents[np.where(absPercents != 0)]))
print("RMSE:", rmse(modelDatapoints, expDatapoints))




