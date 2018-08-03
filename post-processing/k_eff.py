import h5py
import numpy as np
import sys
import os



#argv[1] must be a directory containing one or more .h5 files
for filename in os.listdir(sys.argv[1]):
    totalError = 0
    if sys.argv[1][-1] == '/':
        path = sys.argv[1] + filename
    else: 
        path = sys.argv[1] + '/' + filename
    try:
        f = h5py.File(path, 'r')
    except: 
        pass
    else:
        index = 1
        done = False
        while not done:
            if index < 10:
                state = "STATE_000" + str(index)
            else:
                state = "STATE_00" + str(index)
            index += 1
            try:
                keff = f[state]["keff"][()]
                totalError += (keff - 1) * 10**5
            except:
                print("filename:", filename)
                print("mean k_eff:", totalError / (index - 1))
                done = True
            
    

