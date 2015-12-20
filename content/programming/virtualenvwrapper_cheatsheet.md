Title: virtualenvwrapper Cheatsheet
Date: 2015-12-06 15:18
Slug: virtualenvwrapper-cheatsheet
Authors: Liwen Wen

[TOC]

# Why virtualenvwrapper?
--- 

Sometime we may work on different projects which require different versions of
prerequisite packages, then if you have only on global development environment,
you will run into troubles to manage all of these libraries. virtualenvwrapper
provides a good solution to this kind of dillema by isolating development
environments for different projects. 

# Installation
---

`$pip install virtualenvwrapper` or `$sudo pip install virtualenvwrapper`

# Configuration
---

Add lines to your `.bashrc` or other shell startup files:

    :::sh
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Dev #TODO
    source /usr/local/bin/virtualenvwrapper.sh

The first environment variable `WORKON_HOME` is used to store all of the virtual
environments you create. 

# Quick-start
---

1. Create a virtual environment: `$workon test -p /usr/local/bin/python3.4`

2. Check all installed packages: `$pip freeze` 

3. Install new packages: `$pip install pelican markdown`

4. Quit virtual environment: `$deactivate`


