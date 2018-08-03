<b> Overview </b>
This repository contains models for the benchmark critical experiments performed at the IPEN-MB/01 reactor. 6 different experiments were modelled, each in two and three dimensions. Additionally, this repository contains scripts for submitting the models to run on MPACT through Flux, post-processing scripts to analyze the output and compare it to the experimental data, and scripts to perform sensitivity analysis, where applicable.

<b> How to use </b>
To submit the models to Flux, it is advised to cd into the directory containing the relevant input file and submit the .pbs file from there. The an .h5 and an .xml file will be produced in the experiment's output folder. 

To examine the eigenvalue of a model, run k_eff.py and pass it the path to the directory containing the .h5 file(s) to be analyzed. The code will examine each .h5 file in that directory.

For other post-processing analysis, edit the relevant script and set the value of "pathToTopLevel" to your path to the top-level git directory before running the code. 
