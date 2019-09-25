# Git Workshop
This workshop's purpose is to get you up to speed with basics of git!

## What is Git?
Git is a distributed version-control system for tracking changes in source code during software development. 
It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. 
Its goals include speed, data integrity, and support for distributed, non-linear workflows 
([Wikipedia Git](https://en.wikipedia.org/wiki/Git))

So basically, if you and I are working on the same code, we can:
* make changes **concurrently**,
* keep track of our changes **over time**, 
* **revert to old versions** of our code, and
* systematically **merge eachother's code** into one coherent version (this usually happens automatically unless merge conflicts occur... More on that later).

This tutorial will cover the basics of git:

1. [Cloning](#cloning)
1. [Git Configuration](#git-configuration)
1. [Branching](#branching)
1. [Committing](#committing)
1. [Pushing](#pushing)
1. [Merge Conflicts](#resolving-conflicts)
1. [Rebase/Merge](#rebase-or-merge)
1. [Git Ignore](#git-ignore)
1  [Bonus stuff](#bonus-stuff)

Github Development Tools
1. Issues
1. Kanban Boards
1. Assignees
1. Commits
1. Pull Requests
 * Peer Review

## Cloning
* `git clone [repository name]`
* HTTP vs SSH

## Git Configuration
* Local (Repo) level git config
  * Scoped to the current repository directory you are in
  * `git config user.name=[your_github_username]`
  * `git config user.email=[your_email]`
* Global level git config
  * `--global` scoped to repositories in the home directory
  * `--system` scoped to all repositories in your local filesystem

or do it in vi

* `git config --global --edit`

## Branching
* `git branch`
* `git branch [branch_name]`
* `git checkout [branch_name]`

Or Do it all in one command 
* `git checkout -b [new_branch_name]`
---
We use a branching technique called **Feature Branch**; This means that when you are developing a new [feature], name the branch after that feature and only make [feature] related changes on that branch.

Example: If we need to implement a timelapse for OBC

1. `git checkout -b timelapse`
1. Continue to develop the timelapse on the timelapse branch.
1. Merge the branch when feature is completed(more on this step later).

**What not to do**

1. `git checkout -b dragons-branch`
1. Make hundreds of random changes for 8 months.
1. Merge the branch with all the random changes 2 weeks before competition.

## Staging
* `git add [file_to_be_staged]`
* `git add -p [directory or file]`
	* `-p`: Patch
	* Go through all the changes and select which to stage and which to not stage

## Committing
* `git commit -m "[a description of your commit]"`
	* `-m <message>` specifies `<message>` as the commit message
* Stage and Commit in one command
	* `git commit -a -m "[a description of your commit]"`
	* `-a` Tells the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.
## Stashing
Revert any un-commited changes back to the last commit
`git stash`
* Stash is a stack 
* Pop a stash 

## Pushing
In order to get all of your local changes distributed amongst the team, we need to send those changes to the remote repository.
* `git push`

## Rebase or Merge
* `check what branch your on`
* `git fetch`
* `git merge origin master`
#### OR
* `git pull origin master`

## Resolving Conflicts

## Git Ignore
* `.gitignore`

## Bonus stuff
* SSH key pairs
* Git Aliases ie .bashrc .zshrc
	* [dot files](https://github.com/dragonprevost/dot-files/blob/master/zshrc)
* Git status `git status`
* Git diff `git diff`
