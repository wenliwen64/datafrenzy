Title: Analysis Notes on Phi Yields in AuAu 14.5GeV Collisions
Date: 2015-11-17 01:54
Modified: 2015-11-17 01:54
Slug: phi-15GeV
Authors: Liwen Wen
Status: draft

[TOC]

## Data Set

## Codes Documentation
### Upstream Embedding
----
* Raw Data Files Location: 

     `pdsf$/global/projecta/projectdirs/starprod/embedding/production_15GeV_2014` 

* Make File List: `pdsf$python makelist.py phi flat(exp)`
* How to Configure the Run:
    1. Scripts from low to high: `run.sh` -> `run2.sh` -> `submit_phi.sh`
    2. Change the library version in `run.sh`; 
* How to Run It:
    3. `pdsf$./submit_phi.sh phi auau15GeV_run14_phi_exp.full.list` will create a directory named `output_auau15GeV_run14_phi_exp.full` contatining all of the output files;

### Mid-Downstream Embedding
----
* Location: `/global/homes/l/lwen1990/pwg/embedding/15GeV_embedding/Phi/analysis`
* Codes Files: `cuts_phi.C`
* How to Configure Run: change the `kTrue`/`kFalse` value in `run.C` to select exp/flat data
* How to Run It: `$root -l run.C`
* Output: `mcphiexp.histo.root`(`mcphifp.histo.root`) and `weight_phi_exp.txt`(`weight_phi_fp.txt`), the latter will be used as the efficiency input in downstream data analysis.
* Results: 
    1. [Efficiency]({filename}/plots/final_eff_combined_phi_15GeV.pdf)([fp_data]({filename}/data/weight_phi_fp_15GeV.txt), [exp_data]({filename}/data/weight_phi_exp_15GeV.txt))
    2. [Eff_err Comparison]({filename}/plots/efferr_comparison_phi_15GeV.pdf)

### Upstream Data Analysis 
----
* Location: `/star/u/lwen1990/ucla/v0_15GeV/batchjobs`
* How to Compile `StRoot`: 
      1. `$starver SL14i`
      2. `$cons EXTRA_CPPFLAGS=-fpermissive`
* How to Run It:
      1. `$cd batchjobs`
      2. `$./submit_15GeV_Phi.sh 0901 01 15GeV phi` which will generate data/hists files under `realoutput` directory and the name is like `0901_15GeV_phi_data`. The `01` is the test number.
      3. If you run command like this, you will gnerate rotational files as well if you activate the relevant member function of StRoot in `reconstruct_v0.C`

### Mid-stream Data Analysis
----
Notes: There is no mid-stream analysis code for Phi particle. All you need to do is to compress all of the hsitograms created by StRoot into one file and download it to your local machine.

----
### Downstream Data Analysis
----
* Location: `/Users/lwen/Documents/Omg_Phi_15GeV/Phi/StPhiDownMaker`
* Main File: `/Users/lwen/Documents/Omg_Phi_15GeV/Omega/StPhiDownMaker/StPhiDownMaker.cc`
* How to Compile It: `root -l` + `root[0].L StPhiDownMaker.cc++`
* How to Run It: 
     1. configuration: 
           * datfile -> real data(Compress all of the Up-stream output histogram data, also including mixing event background)
           * efficiency file -> hard coded in `StPhiDownMaker.cc` 
     2. run command: `$root -l run_spectra.C`
* Reults:
     1. [Raw Spectra]({filename}/plots/omg_rawspectra.pdf) ([data]({filename}/data/omg_rawspectra.txt))
     2. [Corrected Spectra]({filename}/plots/omg_finalCorrSpectra.pdf) ([data]({filename}/data/omg_finalCorrSpectra.txt))
     3. [Comparison]({filename}/plots/compare11GeV_omg.pdf) ([data]({filename}/data/compare11GeV_omg.txt))

### Comparison between Xiaoping's and my results on Phi Spectra
---
* Location: `StPhiDownMaker::compare11GeVRawSpectra010()` 
* Main File: `home-linux$~/Downloads/uncorrectedphi/11.5/010.txt`

* Result: [plot]()
