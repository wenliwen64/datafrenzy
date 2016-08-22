Title: Miscellaneous Tips
Date: 2015-12-14 14:01
Slug: miscellaneous-tips
Authors: Liwen Wen
Status: draft

## Some useful information
---
* AuAu200GeV Run11 Data:
    * Period1: <=12138024
    * Period5: 12154021-12165031(Pile-up Protection)
    * Period6: >12165031(?)

* When you cannot compile your previous code(which may work under compiler version 4.7.7), try to use `cons EXTRA_CPPFLAGS=-fpermissive` 

## Q&A
* How to make job run on server background without specific distribution computing facilities?

    Ans: `ctrl+z` and `$bg`, you are good to go.

* How to transfer files on rcf to hpss

    1. "hsi" in rcas to go hpss

    2. "pwd" in hsi it will show ur home in hpss

    3. To transfer files to hpss from source directory (in rcas) just use `htar -Pcf  hpsspath/test.tar dir_in_rcf`, then `dir_in_rcf` will be copied to hpass as `dir_in_rcf.tar`

    4. To extract those: `htar -xf hpsspath/test.tar`

* How to make vim not comment all of the code?

    `:set paste` and then enter insert mode in vim.

* How to get the file list on rcf using get_file_list.pl

    1. [user-manual](https://drupal.star.bnl.gov/STAR/comp/sofi/filecatalog/user-manual)

    2. `get_file_list.pl -keys 'path,filename' -cond 'production=P05ic,trgsetupname=ProductionMinBias,filetype=daq_reco_mudst,filename~st_physics,storage!=HPSS' -limit 10`
