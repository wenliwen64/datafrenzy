Title: Fermi Lab Calorimeter Test
Date: 2016-04-26
Slug: fermi-lab-calor-test
Author: Liwen Wen
---

[TOC]
# Log:

1. Only two ADC blocks, each having 16 channels.

2. To get the pedestal, run disabled `zero-suppression` to get the `pedestal_setting.txt`, then run `zero-suppression` test to get the real signals. 

3. We also have to change the resolution of ADCs, high resolution = low range, so we have to choose the appropriate resolution to record all of the data. 

4. Don't click `Stop DAQ`  

5. To run the `PedestalM.C` we have to change the No. of ADCs(probably we can improve it). 

6. For zero-suppression mode, slot3 and slot7 are wrong for some reason, it is like hardware issue. Check `lw_ped_enabled_slot3_slot7.txt` for details.
