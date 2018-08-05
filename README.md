<b> Overview </b>
This repository contains models for the benchmark critical experiments performed at the IPEN-MB/01 reactor. 6 different experiments were modelled, each in two and three dimensions. Additionally, this repository contains scripts for submitting the models to run on MPACT through Flux, post-processing scripts to analyze the output and compare it to the experimental data, and scripts to perform sensitivity analysis, where applicable.

<b> How to use </b>
To submit the models to Flux, it is advised to cd into the directory containing the relevant input file and submit the .pbs file from there. The an .h5 and an .xml file will be produced in the experiment's output folder. 

To examine the eigenvalue of a model, run k_eff.py and pass it the path to the directory containing the .h5 file(s) to be analyzed. The code will examine each .h5 file in that directory.

For other post-processing analysis, edit the relevant script and set the value of "pathToTopLevel" to your path to the top-level git directory before running the code. 

<b> 2D models and sensitivity analysis </b>
Most two-dimensional models are subdivided further to allow for sensitivity analysis. The models that subdivided in this way are the experiments whose configurations differ only in control rod position, as this cannot be analyzed in two dimensions. Within 2D input directories, directories ending in "_f" consist of input files with a finer mesh. 2D input files ending in "_1" have the axial buckling card set to the lowest value of the uncertainty range for buckling, files ending in "_2" have the nominal axial buckling value, and files ending in "_3" have the highest value of the uncertainty range. 
