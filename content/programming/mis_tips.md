Title: Miscellaneous Tips
Date: 2015-12-14 14:01
Slug: miscellaneous-tips
Authors: Liwen Wen
Status: draft

## How to make job run on server background without specific distribution computing facilities?
- - -

Ans: `ctrl+z` and `$bg`, you are good to go.

## How to transfer files on rcf to hpss
- - -

Ans: 

1. "hsi" in rcas to go hpss

2. "pwd" in hsi it will show ur home in hpss,

For  transfer  to hpss: from source directory (in rcas) just enter the command

    htar -Pcf  hpsspath/test.tar test(directory path in rcf u want to transfer)

"test" dirctory will copied as test.tar in hpss.

To extract those:

    htar -xf hpsspath/test.tar`

## How to make vim not comment all of the code?
- - -

Ans: `:set paste` and then enter insert mode in vim.

## How to get the file list on rcf using get_file_list.pl
- - -

1. [user-manual](https://drupal.star.bnl.gov/STAR/comp/sofi/filecatalog/user-manual)

get_file_list.pl -keys 'path,filename' -cond 'production=P05ic,trgsetupname=ProductionMinBias,filetype=daq_reco_mudst,filename~st_physics,storage!=HPSS' -limit 10
