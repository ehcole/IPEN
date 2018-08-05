#!/bin/bash
echo "case 1: control rods in"
echo
echo "low buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-1_f_r.h5
echo "med buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-2_f_r.h5
echo "high buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-3_f_r.h5
echo
echo "reference:"
echo
echo "low buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-1_r.h5
echo "med buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-2_r.h5
echo "high buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/in/6-3_r.h5
echo
echo "case 2: control rods out"
echo

echo "low buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-1_f_r.h5
echo "med buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-2_f_r.h5
echo "high buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-3_f_r.h5
echo
echo "reference:"
echo
echo "low buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-1_r.h5
echo "med buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-2_r.h5
echo "high buckling"
python ../../../post-processing/reactionRates.py ../outputs/2D/out/6-3_r.h5
