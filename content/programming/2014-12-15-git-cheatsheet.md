Title: Git Cheatsheet
Date: 2015-11-02 14:15
Modified: 2015-11-02 14:15
Category: Programming
Tags: git, cheatsheet
Slug: git-cheatsheet
Authors: Liwen Wen
Status: published

[TOC]

This article is for people who already get familiar with git to certain extent but still need some quick reference at work. 

## Some Key Concepts
---
1. SHA-1 value or so-called checksum is used for reference to commit;

2. master branch is the main branch you are working on;

3. HEAD is the tip of current branch(we may have multiple branches at same time). We can move HEAD around and then start recording. So remember, before you move HEAD pointer, you have to store the `git log master` information properly. Because you will not be able to find them out when you move your HEAD back, i.e., you can find information at HEAD and before HEAD. Maybe you can find the information.? Yes, `git reflog` will give all of the information you need(mainly the SHA-1 value) to do `git reset HEAD SHA-1`

4. Snapshots instead of Changes: Git is storing the snapshots of projects status in different commit instead of the changes regarding each files. So if one file stays unchanged from last commit, git will only store the pointer pointing to it in last commit. Not like other version control system which will only record the difference of each file in each commit.

5. The three states: There are three main sections in a git projects: the Git directory, the working directory, and the staging area: 1. Git directory: place for Git to store the metadata and object database for your project. Basically you copy this directory when you are cloning a repository; 2. Working directory: this is a single checkout of one version of the project. You can add or modify files whatever your want; 3. Staging area: staging area is a file where stored winofrmation about what will go into your next commit. It is sometimes referred to as "Index"

6. Basic Git workflow: 1. You modify files in your working directory; 2. You stage the files, adding snapshots of them to your staging area; 3. Commit those changes, which takes the files as they are in the staing area and stores that snapshot permanently to your git direcitory

7. Some terms: 1. `committed`: a particular version of a file is in the Git directory; 2. `staged`: the modified file is added into the staging area; 3. `modified`: If a file was changed since it was checked out but has not be staged, it is called modified

## Handy Commands
---
3. To show the changes between working directory and staged changes:
   `$git diff` is working vs. cached(staged);
   `$git diff -cached commit_sha` is staged vs. commit;
   `$git diff commit_sha` is working vs. commit.

4. In `git diff`: `---` and `+++` mean old version and new version

5. Use `git rm` and `git mv` to delete and rename files. Because if you only use `/bin/rm`, you will also have to `git add` these files. `git rm` does this in one step.

6. `git checkout -- index.html` ???

7. `git reset HEAD file.txt` is to rest the file.txt(staged) back to HEAD state, this doesnt affect the working directory.

8. ??? `git checkout SHA-1 -- filename`

9. `git revert HEAD-3` is to apply opposite changes and commit a new commit.

10. Use `merging` instead of `revert`

11. `git reset --soft SHA-1` just changes the HEAD position;

12. `git reset --mixed SHA-1` is taking something to staged directory.

13. `git reset --hard SHA-1` is taking something to staged directory and working direcotry.

14. Add `!index.html` to eliminate the file from ignore file list.

15. `git log -p SHA-1` is to see the difference

16. `git dif sha..sha` is to compare the two commits.

17. `git merge branch1` is to merge branch1 into master.

18. `git branch -m branch_old branch_new` is to rename and `git branch -d branch_to_delete`  is to delete the branch.

19. `git merge --abort` is to abor the merge. If not, you have to fix the conficts and do the commit to finish merging.

20. `git remote add origin https://.......` is to add the remote repository with alias `origin`.

21. `git push -u origin master` is to push the `master` branch to remote repository and keep tracking it. "keep tracking" means when other ppl do fetch they can see this branch.

22. `git branch -r` is to show the remote branches; `git branch -a` is to show all branches. 

23. `git clone` is to copy the repository like when you are going to contribute to open source project.

24.  `git pull` = `git fetch` + `git merge origin/master` is to merge the remote HEAD to your current branch. 

25. `git push origin non_tracking:non_tracking` is to rename the branch name; so `git push origin :non_tracking` will delete the `non_tracking` branch;

26. `git log -p feedback..origin/feedback` is to compare the remote and local repository

27. `git rm --cached filename` is to remove file from index.

## Integrated Collaboration Workflow
---
Sometime we can use this workflow between different machines we are working on...

Me:

    :::sh
    > git checkout master
    > git fetch
    > git merge origin/master 
    > git checkout -b feedback_form
    ...do some stuff
    > git commit -am "Add customer feedback form"
    > git fetch
    > git push -u origin feedback_form   # -u is for the first time

Lynda:

    :::sh
    > git checkout master
    > git fetch
    > git merge origin/master 
    > git checkout -b feedback_form origin/feed_back
    > git log
    > git show 84b6adf0
    ...do some stuff
    > git commit -am "Add tour sector to feedback form"
    > git fetch
    > git push  

Me:

    :::sh
    > git fetch
    > git log -p feedback_form..origin/feedback_form
    > git merge origin/feedback_form
    > git checkout master 
    > git fetch
    > git merge origin/master
    > git merge feedback_form
    > git push

## Some Awkward Scenarios to Deal with
---
1. If you mistakenly commit a big file, what you can do to fix it?



      :::sh
      > git 

2. How to move or remove files?

## Undoing Things
---
### Uncommit things:

*Scenario 1*: You commit something too early and possibly forgoet to add some files, or you mess up your commit message:

    :::sh
    > git commit  -m 'initial commit'
    > git add forgotten_file
    > git commit --amend

These commands will make you end up with a single commit which contains all of the changes and the second commit will overwrite the previous one.

### Unstage things: 

*Scenario 2*: You changed two files and want to commit them separately. But you accidently type `git add *` and stage them both. So how to unstage them?

    :::sh
    > git add * 
    > git status
    On branch master
    Changes to be committed:
    (use "git reset HEAD &lt;file&gt;..." to unstage)

    renamed:    README.md -> README
    modified:   CONTRIBUTING.md
    reset the CONTRIBUTING.md file
    > git reset HEAD CONTRIBUTING.md
    Unstaged changes after reset:
    M   CONTRIBUTING.md
    > git status
    On branch master

    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md

### Unmodifying a Modified File
*Scenario 3*: What if you realize that you don't want to keep your changes to the CONTRIBUTING.md file? Or you just easily revert it back to what it look when you last commit?

    :::sh
    > git checkout -- CONTRIBUTING.md
    > git status
    On branch master
    Changes to be committed:
    (use "git reset HEAD &lt;file&gt;..." to unstage)

    renamed:    README.md -&gt; README

Note: this is kinda dangerous since it will discard anything changed. 

### Usage of git-stash
*Scenario 4*: When you have been working on part of your project, things are in messy state but you want to switch branches for a bit to work on something else.You dont want to do a commit. 

    :::sh
    > git status
    Changes to be committed:
    (use "git reset HEAD &lt;file&gt;..." to unstage)

    modified:   index.html

    Changes not staged for commit:
    (use "git add &lt;file&gt;..." to update what will be committed)
    (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)

    modified:   lib/simplegit.rb



So next step is to issue the `git stash` command

    :::sh
    > git stash
    Saved working directory and index state
    "WIP on master: 049d078 added the index file"
    HEAD is now at 049d078 added the index file
    (To restore them type "git stash apply")

Now the working directory is clean, i.e., you can switch branches:

    :::sh
    > git status
    # On branch master
    nothing to commit, working directory clean

Check the stash list:
   
    :::sh
    $ git stash list
    stash@{0}: WIP on master: 049d078 added the index file
    stash@{1}: WIP on master: c264051 Revert "added file_size"
    stash@{2}: WIP on master: 21d80a5 added number to log

Come back to previous state(`git stash apply stash@{2}`): 

    :::sh
    $ git stash apply
    # On branch master
    # Changed but not updated:
    #   (use "git add &lt;file&gt;..." to update what will be committed)
    #
    #      modified:   index.html
    #      modified:   lib/simplegit.rb
    #

## Git Submodules
---
Usually, we need external library to be included in your working project. Otherwise customer of your software would need to download the shared lib you used. In this site, I have two separate subdirectories(pelican-themes, pelican-plugins) to be submodules. The workflow is like below:
 
   1. Fork the `getpelican/pelican-themes` and `getpelican/pelican-plugins`;

   2. In your working directory or parent directory, `git submodule add git@github.com:wenliwen64/pelican-themes` and `git submodule add git@github.com:wenliwen64/pelican-plugins`;

   3. You can check the file `.gitmodules` where store the information about where is the remote repository for the submodule;

   4. Go into your submodule directory, apply commands `git submodule init` + `git submodule update`;

   5. Change directory to parent directory and `git push origin master --recurse-submodules==on-demand`;

   6. On another machine, do `git clone git@github.com:wenliwen64/pelican_site.git --recurse`;

   7. If you want to make change to the themes you have to fork it on github first. 

## Git conflict resolution
---

