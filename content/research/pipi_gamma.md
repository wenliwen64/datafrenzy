Title: Pipi Gamma
Date: 2015-11-30 12:29
Slug: pipi-gamma
Authors: Liwen Wen

[TOC]

# Data 
---
0. Raw Data Location: `/media/Disk_Chen/Data/200GeV_run11/data_minbias5_new/*.flow.nt.root`
1. Generated Data Location: `lwen@giant:/home/lwen/Analysis/pi_pi_gamma/Cen*/*root`

# Code
---

Please check repository: https://github.com/wenliwen64/pipi_gamma.git

# Running Instruction
---

i. `$cd pipi_gamma/StLPVPlotMaker`

ii. `$root -l run.C`

Notes: You can change the centrality number in `run.C: maker->Init(n_cen, n_jobs)`

# Toy Monte Carlo Model

simulation study on MSC observable with Fuqiang's method.

some questions:
   1. Why use two subevents, one for event plane reconstruction and one for v2 calculation?

   Ans: stupid if you use the full event plane you will get positive v2, if you define the event plane orientation by $\Phi_{ep} = atan2\frac{\sum_i w_i sin2\phi_i}{\sum_i w_i cos2\phi_i}/2$!
   2. 
The Modulated Sign Correlator(msc) is defined as below:

$$msc = (\frac{\pi}{4})^2(\lt S_\alpha S_\beta\gt_{in} - \lt S_\alpha S_\beta\gt_{out})$$

Explanation: 
    1. $S_\alpha S_\beta$ is standing for the cos term sign of correlated particle $\alpha$ or $\beta$    

Procedures: 

    1. Input the rp orientation = 0;  

    2. QA histograms:

        i. `TH1D* hmsc = new TH1D()` to get the distribution of msc so that we can check if the gamma is close the value of msc.  east/west ep, west/east v2, compute msc 

        ii. `TH2D* hmsc_v2 = new TH2D()` so that you may fill this by `hmsc_v2->Fill(east_v2, msc)` event-by-event

# Log

# Data Points
----

## AuAu200GeV MinBias5 Run11 Data
                     
1. [Gamma]({filename}/data/gamma_pipi_auau200GeVminb5Run11.txt)

2. [Delta]({filename}/data/delta_pipi_auau200GeVminb5Run11.txt)

3. [Kappa_killer]({filename}/data/kk_pipi_auau200GeVminb5Run11.txt)
