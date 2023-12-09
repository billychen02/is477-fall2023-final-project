# Analaysis of UCI Diagnostic Breast Cancer Data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10311477.svg)](https://doi.org/10.5281/zenodo.10311477)

## **Overview:**
The purpose of this repository is to reproduce the results reported of the "Breast Cancer Wisconsin (Diagnostic)" by Wolberg, W., Mangasarian, O., Street, N., and Street, W. (1995), utilizing UC Irvine Machine Learning Repository. The data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass, indicating the traits and characteristics of the nuclei cell captured in the image. The analysis will evaluate 10 corresponding features that influenced the tumor cell analysis: radius, concavity, compactness, texture, perimeter, area, smoothness, concave points, symmetry, and fractal dimension. The first three factors are selected for further analysis and visualization to determine the differences between benign and malignant tumors. We have also calculated and included the summary statistics that indiicates the mean, median, and standard deviation for all 30 corresponding factors.

## **Contributions:**
Peter - Peter has contributed to the most of the analysis and elaboration of the Readme file, explaning each steps of analysis and put into words. He also works extensively with the visualization part (step 9) and work together with Billy on the Random Forest Classification coding and result interpretation.

Billy - Billy has contributed extensively from step 5 to step 8 (write a script prepare_data, profile, analysis, and create Snakefile) and the virtual environment section. He has worked with Peter on the coding and classification part to create the random forest classification model. He also responsibles for creating the zenodo.json and integrate that with our Github repository.

## **Analysis:**

We have performed random forest classification to train breast tumor data to identify and predict whether the tumor is malignant (cancer), using several correlated predicted factor, as well as observing the characteristics of tumor cells: redius, compactness, and concavity. We have found that the precision of both benign and malignant classifications are significantly high (>0.9), as well as the recall and f-1 score for both, indicating the high efficiency of the analysis. We have also found that the compactness and cocavity of both types of tumors are approximately equal, however, the radius of malignant tumor is significantly higher than that of benign, on average. This indicates the likelihood of identifying cancer tumor call by analyzing the cell's radius.

## **Workflow:**

![Visualization of the workflow graph] (https://edotor.net/?engine=dot#%23%20Place%20the%20cursor%20inside%20%22graph%22%20to%20get%20some%20refactoring%20options%0A%0Adigraph%20G%20%7B%0Arankdir%3DTB%0Afontname%3DCourier%3B%20fontsize%3D18%3B%20labelloc%3Dt%0A%0Anode%20%5Bshape%3Dbox%20style%3D%22filled%2C%20rounded%22%2C%20fillcolor%20%3D%20%22%23FFFFD1%22%5D%0A%22data%5Cwdbc.data%22%0A%22data%5Cwdbc.names%22%0A%22data%5Cwdbc.data%22%0A%22profiling%2Freport.html%22%0A%22data%5Cwdbc.data%22%0A%22results%2FBM_comparison.png%22%0A%22results%2Ffeature_importance.png%22%0A%22summary_stats.csv%22%0A%22wisconsin_breast_cancer_analysis.txt%22%0A%0Anode%20%5Bshape%3Dbox3d%20style%3D%22filled%2C%20rounded%22%2C%20fillcolor%20%3D%20%22%23D6FDD0%22%5D%0A%22analyze%22%0A%22prepare%22%0A%0Aedge%20%5Bcolor%20%3D%20black%5D%0A%22data%5Cwdbc.data%22%20-%3E%20%22profile%22%0A%22data%5Cwdbc.data%22%20-%3E%20%22analyze%22%0A%22prepare%22%20-%3E%20%22data%5Cwdbc.data%22%0A%22prepare%22%20-%3E%20%22data%5Cwdbc.names%22%0A%22profile%22%20-%3E%20%22profiling%2Freport.html%22%0A%22analyze%22%20-%3E%20%22results%2FBM_comparison.png%22%0A%22analyze%22%20-%3E%20%22results%2Ffeature_importance.png%22%0A%22analyze%22%20-%3E%20%22summary_stats.csv%22%0A%22analyze%22%20-%3E%20%22wisconsin_breast_cancer_analysis.txt%22%0A%0A%7D%0A)

## **Reproducing:**

For reproducing the results from this repository, here are some things to set up before the action. 
<ol>
<li>Environment Check: Open the environment.log file in the repository to view details of specific libraries and versions used such as the system type, system version, python version to make sure you are on the write platform to use the codes. </li>

<li>Dependencies Installation: Install the dependencies using "pip install -r requirements.txt". </li>

<li>Datasets Acquisition: After setting up your machine with the right dependencies and versions (could use virtual environment to do so for the older version of python for this specific project for the report making), open the "prepare_data" script and run it using the right python version and it will provide you with the exact files needed for the reproduction of the results in this repository.An important addition made to the data was that after you manually unzip the file downloaded with prepare_data.py, you will have to manually add a line before the beginning of the wdbc.data with the corresponding column names so that the rest of the functions and dataframe making with Pandas will run smoothly since the dataset comes in as pure data csv file with any data labels or naming. But this information of each column is provided on the UCI website when acquiring for the breast cancer dataset. </li>

<li>Reproducing the profiling report: To create the report.html, we utilize a python package called ydata profiling. They offer a function called profile report that turns your dataframe or your data into a html report that you can view via browsers.Once you unzip the file from the downloaded, the script automatically uses the default unzip name of the .data file and turn it into a report for further usage in the profiling folder. </li>

<li>Reproducing the analyses and plots using scripts: To create the two png files of the graph, summary_stats.csv and the results given for you in the wisconsin_breast_cancer_analysis.txt, you will need to use the analyze.py scripts. All the process is relatively automatic after you manually unzip the file in the "data" folder, the scripts will import all the packages you need after you download the dependencies in the requirements and perform the calculation and plotting to the "results" folder as needed. </li>

<li>Reproducing the the workflow diagram: We have utilized the dag.py file to create the DOT file, and then we ran all the codes, and migrarte the output to the edotor.net website to create the digraph for the visualization purpose.The visual of the workflow diagram will then be produced and you can share it by copying the share link in the edotor.net website and paste it on github with image embedding markdown. </li>

</ol>

## **Licenses:**

Software licensing

We will be using the MIT License since it is one of the most adopted permissive license with standardized regulations and policies and can be applied to different types of dataset. Created by Massachusette Institute of Technology, the license is free of charge for seamless using, copying, associated documenting, sublicensing, publishing, merging, distributing and modifying the data. The reproducibility and replicatability function of this license will enable future utilization of this data and of our analysis in the future project. Additionally, the MIT also includes the limited liability feature, which providing the legal protection to the owners and reproducers of the data and software.

Data licensing

## **References:**

Data citation
- Wolberg,William, Mangasarian,Olvi, Street,Nick, and Street,W.. (1995). Breast Cancer Wisconsin (Diagnostic). UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B.

