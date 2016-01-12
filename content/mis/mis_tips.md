Title: Miscellaneous Tips
Date: 2015-12-14 14:01
Slug: miscellaneous-tips
Authors: Liwen Wen

[TOC]

---
1. How to make job run on server background without specific distribution computing facilities?

Ans: `ctrl+z` and `$bg`, you are good to go.

## How to transfer files on rcf to hpss
> enter "hsi" in rcas to go hpss
> "pwd" in hsi it will show ur home in hpss,
For  transfer  to hpss: from source directory (in rcas) just enter the command

htar -Pcf  hpsspath/test.tar test(directory path in rcf u want to transfer)

"test" dirctory will copied as test.tar in hpss

to extract those:
htar -xf hpsspath/test.tar
