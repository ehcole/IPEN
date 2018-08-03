#!/bin/bash
echo "low buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009bm/IPEN-009-1p.h5
echo "med buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009bm/IPEN-009-2p.h5
echo "high buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009bm/IPEN-009-3p.h5
echo
echo "reference:"
echo
echo "low buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009b/IPEN-009-1.h5
echo "med buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009b/IPEN-009-2.h5
echo "high buckling"
python /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/analysis/pinPowers.py /scratch/wrm_fluxoe/ehcole/IPEN_Analysis/version2/IPEN-009b/IPEN-009-3.h5
