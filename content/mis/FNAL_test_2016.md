Title: FNAL EMC test
Date: 2016-05-01
Slug: fnal-emc-test
Author: Liwen Wen

[TOC]

# Analysis Code:
---
1. `EIC_EM_combined.C`: used to plot multiplicity vs. energies and resolution vs. energies. 

2. `PedestalM.C`: change the nadc in line 41. Input: `test.txt`, `test1.txt`, `test2.txt` which are corresponding to high-medium-low-resolutions. Output: `pedestal_setting.txt`.

3. `ReadoutDataM.C`: used to plot ADC channel spectra. 

4. `EIC_macros/ReadoutHistograms.C` or `EIC_macros/ReadoutHistogramsNewECal.C`: Input: data188.txt. Output: data188.txt.root

5. `NewECalCalibration.C`: Input: `.root`. Output: plots. Tune cuts in the middle.

6. `NewECalAnalysis.C` or `NewECalAnalysis1.C` or `NewECalAnalysis2.C`: Input: `.root` files. Output: histograms.

7. TODO: add the setup diagram.

# Summary 
---
All of the code is under directory `Documents/2016_FNAL_test/macros_2016`

## Sdata: Spaghetti detector with 10 degrees

1. Data: `20160506`

2. Code: `ReadoutData_2016.C` to check the raw data; `ReadoutHistogramsNewECal_2016.C` to convert the raw `.txt` files to `.root` files;  `NewEcalAnalysis_wide_cuts_batch.C` to analyze data, plot spectra from Lead glass or our carolimeter, uniformaty map, deposited energy profile along each side, this script cannot be run alone, you have to modify the `batch_regular.C` to input the data set files for analysis; `pllot_macros_2016.C` to plot summary resolution plots and mean values' linearity. 

3. Every other directory other than mentioned are corresponding to different data sets, like `old_detector`, `4degree`, `rotate`(data set after rotating the crack orientation). 

4. `report` directory has the report file and all of the plots attached can be found in word file.

5. For `Sdata` and `rotate` data, I already changed the code for pedestal subtraction in `NewEcalAnalysis_wide_cuts_batch.C`, others if I didn't change the script, the resolution data should be fine still.
