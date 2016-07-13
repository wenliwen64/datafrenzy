Title: Chiral Effects with PID correlations
Date: 2016-02-03 10:31
Slug: chiral-effects-with-pid-correlations
Authors: Liwen Wen
Status: draft

[TOC]

# Data
- - - 

## Experiment Data
- - -

   * Period 5: Giant:/media/Disk_Yan/liwen/Run11_200GeV/ && Giant:/home/lwen/(this location should be changed to old_home after last August we changed the hard drive) && Giant:/media/Liwen/Run11_200GeV/ 
   * [Feng Zhao's files location]({filename}/data/feng_files.txt)

## Embedding Data
- - -
 
   * Raw Data Location(on pdsf farm): 

     `/global/projecta/projectdirs/starprod/embedding/AuAu200_production_2011`

     Note: this is the raw data, the `*.geant.root` filelist can be found at 

     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/mid_production`. 

      The python code to generate these lists can be found at 

     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/macro_lib/makelist_auau200GeV_run11_geant_la_antila.py` 

   * Picodst Data Location(on pdsf farm): 
   
     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/data/*full.picodst.root`

     Note: I `hadd` all of the files inside the 

     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/mid_production/output_fp(output_exp)`

# Analysis code for experiment data
- - -

## Upstream:
- - -

   * Location: rcf:/star/u/lwen1990/gpfs/v2_Lambda_200GeV/batchjobs/generate_Period1.sh

   * Note: Every time you update your source code or change your location, you have to update the version number in `Scheduler_new.xml` to make it work as expected. To compile it, just use `starver SL11d` and `cons CPP_EXTRAFLAG=-fpermissive`.

## Downstream:
- - -

   * Location: 

     Feng's code:

     `giant:/home/lwen/Analysis/CVE_project/Period5_Feng/HBT_NotExcluded/Lambda/`; 

     my code: 

     `giant:/home/lwen/Analysis/chiral_code/StProtonLaGammaMaker`(for $\Lambda-p(\bar{p})$) and 

     `giant:/home/lwen/Analysis/LambdaBar/StProtonLaGammaMaker`(for $\bar{\Lambda}-p(\bar{p})$).

   * How to run it: 

     `$root -l runner.C`, but you have to change the event number you want to process inside `runner.C`(0 means process all of the events);

   * Notes: 

      * `eff_test.C` is used to test the `StEffMaker` and its subclasses.

      * If you want to decrease file loading time you can comment out part of the `***->Add()` in `StCorrelationMaker.cpp`;

      * `constants.h` is used to store the cuts for $\Lambda$ and protons and other values like correction orders;

      * `runner_test.C` is obsolete runner for test use only. 

      * If the `StTpcTofEffMaker` or `StErfEffMaker` are not initialized, they will output 1.0 for each efficiency request.

      * For QA purpose you can use code on local machine(MacBook Pro) `/Users/lwen/Documents/chiral_code/local_test/qa_plots.C` to check the v2 of protons and $\Lambda$s or you can add anything you want to check to this code. 

# Analysis code for embedding data
- - -

## Upstream:
- - -    

   * Location: `lwen1990@pdsf:/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/mid_production/StRoot`, the passcode can be found in Chrome(NIM) browser;

   * How to run it: `starver SL11d`; `cons EXTRA_CPPFLAGS=-fpermissive`; `qsub_script_la.sh`; you have to change some parameters in the `qsub_script_la.sh`;

   * Output: `lwen1990@pdsf:/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/output*`, you can compress all of the files into one file and <del>download to local machine for further analysis</del>;

## Midstream:
- - - 

   You can only analyze data midstream on pdsf or rcf because of the software environment(`StPhysicsHelix.h`, `StThreeVector.h`...)

   * Location(on pdsf): 

     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/macro_lib/run_la(antila)_eff_analyzer.C` 

   * How to run it: `root -l run_la_eff_analyzer.C`

   * Output: 

     `/global/homes/l/lwen1990/pwg/embedding/Lambda_2016Summer/data/(anti)la_flat(exp).eff.histo.root` 

## Downstream:
- - -

   Do it locally, because you need to plot a lot of QA plots and internet slows this process. Download the `*eff.histo.root` to local machine 

   `/Users/lwen/Documents/CVE_Project/eff_analysis/auau200GeV_run11_Lambda`

   * Code: `fiteff_la(antila).C`; `run_fiteff.C` under the above directory;

   * How to run it: `root -l run_fiteff.C` and it will generate all of the plots and the data file you need to upload to giant to integrate into Gamma analysis.

   * Output: `../figures/` has some plots to check the fitting and `../data/auau200GeV_run11_la(antila)_eff_comb.fit.dat`. These output files(`*comb*`) should be fed into `StErfEffMaker` to compute the efficiency in gamma computation.

   * Notes for proton efficiency:

      * I obtained the tracking efficiency for protons(anti-protons) from Gang;  

      * I analyzed the TOF Matching efficiency for proton(anti-protons) on giant: 

        `/home/lwen/Analysis/auau200GeV_run11_proton_eff` by running `run_calEffProton.C`;

      * I re-organized the data and fit it with a `pol0` function in 

        `/Users/lwen/Documents/CVE_Project/eff_analysis/auau200GeV_run11_Proton/protonEff`;

      * Upload the generated `dat` file to `giant` for real data analysis.

- - -
# Log
- - -
* 2016-02-03: $Lambda$-p correlation

* 2016-02-04: We need to add new bad run for $Lambda$-p correlation

* 2016-02-08: Begin running code to generate data for Period 1 on rcf(day132-140, 126-128 undone yet).

* 2016-04-08: Check the generated data's leaf `mNoTracks` whether or not corresponds to primary tracks / PtV0s.

* 2016-05-20: Nasim's publication on Lambda and proton's [v2](https://drupal.star.bnl.gov/STAR/publications/centrality-and-transverse-momentum-dependence-elliptic-flow-multi-strange-hadrons-and-p).

* 2016-05-24: Embedding data of $\Lambda$ and $\bar{\Lambda}$ on pdsf: 

    `/global/projecta/projectdirs/starprod/embedding/AuAu200_production_2011`

* 2016-05-24: Read through `StMcEvent` and `StAssociationMaker` documents, figured out roughly how embedding works: basically, it looks through the `TrackNodes` which exists inside `StEvent`, since we don't have `StMuDstMaker` in chain, so we cannot access the container of all global or primary tracks, then store those having MC parterners(not necessarily only one) in the vectors, and then looking for if there is real MC event($\Lambda$), if so, reconstruct them by applying topology cuts and compare to see if those cuts killed them or not; for MC events, you have to store all of the mc events in your tree. 

* 2016-05-25: Rapidity cut for data and monte carlo?(we applied 1.0 eta cut for v0s)

* 2016-05-25: `20143801` is the tag of embedding request created by Feng Zhao in August 2014(there are a few Lambda requests for run11 auau200GeV data existing on pdsf). All info. about this request can be found [here](https://drupal.star.bnl.gov/STAR/starsimrequests/2014/sep/19/embedding-requests-k0s-antilambda-run11-auau-200gev)

* 2016-05-28: Why we cut proton on 2GeV/c for upper limit? For the tpc tracking precision or Jets influence. Why we cut the lower

* 2016-06-02: The issue remaining in protons efficiency study is Centrality 7 has an suspicious `enhancement` in low pt range for TOF matching efficiency. Also I just roughly fit it with small fraction of data. 

* 2016-06-02: 200GeV: Period1(12123~ - 12138~), Period5(12154~ - 12165~), Period6(12165~ - 12171~); 39GeV: 11098-11112
