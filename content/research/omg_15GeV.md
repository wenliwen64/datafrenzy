Title: Analysis Notes on Omega Yields in AuAu 14.5GeV Collisions
Date: 2015-11-13 10:47
Modified: 2015-11-13 10:47
Slug: omg-15GeV
Authors: Liwen Wen
Status: draft

[TOC]

## Data Set
----
### Production Detatils
----
* Trigger Set: [production_15GeV_2014](http://www.star.bnl.gov/public/comp/prod/prodsum/production_15GeV_2014.P14id.html) 
* Collision: AuAu 14.5GeV 
* Year of Data Taken: year2014
* Production Tag: P14ii

### Event Cuts 
----
* Triggers Used:  

## Embedding Analysis
----
### Upstream 
----
* Raw Data Files Location: 

     `pdsf$/global/projecta/projectdirs/starprod/embedding/production_15GeV_2014` 

* Make File List: `pdsf$python makelist.py omg(omgbar) flat(exp)`
* How to Configure the Run:
    1. Scripts from low to high: `run.sh` -> `run2.sh` -> `submit_omg.sh` -> `qsub_script_omg.sh`;
    2. Change the library version in `run.sh`; 
    3. Change the filelist in `run.sh` if you want to run different dataset;
    4. Change the `1-503` in `qsub_script_omg.sh` so that `10*503` is bigger enough than the total number of input files.
* How to Run It:
    1. `pdsf$./qsub_script_omg.sh`

### Mid-Downstream 
----
####Omega
----
* Location: `/Users/lwen/Documents/Omg_Phi_15GeV/Omega/embedding/analysis`
* Input Files: `mc_exp_omg_15GeV.picodst.root` and `mc_fp_omg_15GeV.picodst.root`, which are hadd files of the `StRoot` output on pdsf
* Codes Files: `cuts_omg_manyptbinseff.C`
* How to Run It: `$./run_cuts_many_omg.sh exp/flat` or `$./run_cuts_many_omgbar.sh exp/flat`
* Output: `mcomg_exp.manyeff.histo.root` or `mcomg_fp.manyeff.histo.root`, these two files will be used as input in downstream analysis in `../../StrAnalyMaker/`

####AntiOmega
----
* Location: /Users/lwen/Documents/Omg_Phi_15GeV/AntiOmega/embedding/analysis
* Input Files: `mc_exp_omgbar_15GeV.picodst.root` and `mc_fp_omgbar_15GeV.picodst.root` which are hadd files of the `StRoot` output on pdsf
* Codes Files: `cuts_omgbar_manyptbinseff.C`
* How to Run it: `$./run_cuts_many_omgbar.sh exp/flat` 
* Output: `mcomgbar_exp.manyeff.histo.root` or `mcomgbar_fp.manyeff.histo.root`, these two files will be used as input in downstream analysis in `../../StrAnalyMaker/`

## Data Analysis
----
### Upstream 
----
#### Omega(AntiOmega)
----
* Location: `rcf$/star/u/lwen1990/ucla/Code_Omega`
* How to Compile: 
      1. `$starver SL14i`;
      2. `$cons EXTRA_CPPFLAGS=-fpermissive`;
      3. back the original version of `StRoot` to `StRoot.bak`, current `StRoot` is used to generate rotational background with different angles;  
* How to Run:
      1. `$cd batchjobs`
      2. `$./submit_15GeV_strangeness.sh 0901 01 15GeV omg` which will generate data/hists files under `realoutput` directory and the name is like `0901_15GeV_omg_data`. The `01` is the test number.
      3. If you run command like this, you will gnerate rotational files as well if you activate the relevant function in `reconstruct_v0.C`

### Mid-stream 
----

#### Omega(AntiOmega)
----
* Location: `rcf$/star/u/lwen1990/ucla/Code_Omega/local_analysis_code`
* Main File: `rcf$/star/u/lwen1990/ucla/Code_Omega/local_analysis_code/omg_mid_analysis.C` and `rcf$/star/u/lwen1990/ucla/Code_Omega/local_analysis_code/plot_overview.C`(for overview event number counting and QA purpose)
* How to Run It: 
       1. `$root -l`; 
       2. `root[0].L StRefMultCorr.cxx++`;
       3. To run data analysis: `root[1].x omg_mid_analysis.C++("0819_all_omg_list","0820_2015_omg")` or `root[1].x omg_mid_analysis.C++("0819_all_antiomg_list","0820_2015_antiomg")`;
       4. To run overview: `root[1].x plot_overview.C++`;

Or:
       1. `$root -l run_mid_analysis.C`(this is a quick runner, quite conviniently!) 

* Results:
TODO: to convert the omg_mid_analysis.C to a "non-parametric" function so that we can compile it in ALic, and write a runner to load it and run it. 

#### Event Counting
----
* Location: `/star/u/lwen1990/ucla/Code_Omega/local_analysis_code`
* Main File: `plot_overview.C`
* Configuration: change the output filename in `plot_overvew.C`
* How to Compile and Run It: `root -l` + `root[0].x plot_overview.C++`
* Results: Like `0820_overview.histo.root` will be generated. 

#### Rot. Bg.
----
* Location: `rcf$/star/u/lwen1990/ucla/Code_Omega/local_analysis_code`
* Main File: `rcf$/star/u/lwen1990/ucla/Code_Omega/local_analysis_code/omg_mid_analysis.C`(for applying tighter cuts)
* How to Run It: 
       1. `$root -l`; 
       2. `root[0].L StRefMultCorr.cxx++`;
       3. `root[1].x omg_mid_analysis.C++("0819_all_omgrot_list","0820_2015_omgrot")` or `root[1].x omg_mid_analysis.C++("0819_all_antiomgrot_list","0820_2015_antiomgrot")` (The arguments within parenthese are the for demostration only);
* Results: root files like `0820_2015_omgrot.mid_analysis.root`;

### Downstream 
----
#### Omega
----
* Location: `/Users/lwen/Documents/Omg_Phi_15GeV/Omega/StrAnalyMaker`
* Main File: `/Users/lwen/Documents/Omg_Phi_15GeV/Omega/StrAnalyMaker/StrAnalyMaker.cc`
* Compilation: `$root -l` + `root[0].L StrAnalyMaker.cc++`
* How to Run It: 
     1. configuration: 
           * overvewfile -> event number
           * datfile -> real data
           * rotfile -> rotational background
           * fpefffile -> flat distributed pt efficiency(fine pt bin) 
           * expefffile -> exponentially distributed pt efficiency(fine pt bin)
     2. run command: `$root -l run_spectra.C`
* Reults:
     1. [Raw Spectra]({filename}/plots/omg_rawspectra.pdf) ([data]({filename}/data/omg_rawspectra.txt))
     2. [Corrected Spectra]({filename}/plots/omg_finalCorrSpectra.pdf) ([data]({filename}/data/omg_finalCorrSpectra.txt))
     3. [Comparison]({filename}/plots/compare11GeV_omg.pdf) ([data]({filename}/data/compare11GeV_omg.txt))
     
#### AntiOmega
----
* Location: `/Users/lwen/Documents/Omg_Phi_15GeV/AntiOmega/StrAnalyMaker`
* Main File: `/Users/lwen/Documents/Omg_Phi_15GeV/AntiOmega/StrAnalyMaker/StrAnalyMaker.cc`
* Compilation: `$root -l` + `root[0].L StrAnalyMaker.cc++`
* How to Run It:
     1. configuration: check Omega case
     2. run command: `$root -l run_spectra.C`
* Reults:
     1. [Raw Spectra]({filename}/plots/omgbar_rawspectra.pdf) ([data]({filename}/data/omgbar_rawspectra.txt))
     2. [Corrected Spectra]({filename}/plots/finalCorrSpectra_omgbar.pdf) ([data]({filename}/data/omgbar_rawspectra.txt))
     3. [Comparison]({filename}/plots/compare11GeV_omgbar.pdf) ([data]({filename}/data/compare11GeV_omgbar.txt))

## TODO List
* Elaborate how to get overview root file
* rcf codes have been moved to `/star/u/lwen1990/gpfs`, I have to rewrite some path variable in some codes.
* The 5 data sets of rotational backgrounds on rcf:
   1. 1130 -> $2\pi/5$
   2. 1201 -> $2\cdot2\pi/5$ 
