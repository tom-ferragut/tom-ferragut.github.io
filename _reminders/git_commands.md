---
title: Git commands
---

A reminder for some `git` commands: from the most basic ones to the ones we think we'll use but we all know the truth...

## Basics

* Create a `.git` in a repository

```sh
git init
```

* Clone a remote repository

```sh
git clone <url>
```

* get the basic informations

```sh
git log/version/status
```

* Modifications between two versions

```sh
git diff #last version
git diff <hash1>..<hash2> #modifications between two separate versions
```

* Get the remote modifications

```sh
git pull
```

* Send your local modifications

```sh
git push #add --force to force push modifications (careful destructive!)
```

* Stage files

```sh
git add #git add . to add everyone
```

* Make a commit

```sh
git commit -m "message"  #-a to commit all
```

* Create a branch

```sh
git branch <name>
```

* See branches (local and remotes)

```sh
git branch -a
```

* Move on the workflow

```sh
git checkout <namebranch>
git checkout <hashcommit>
git checkout HEAD@{n} #move HEAD of n commits back
```

* Merge branches

```sh
git merge <branch> #merge the branch where you are with <branch>
```

## Make modifications onto the workflow

* Rebase a branch

**NB: To handle merge conflicts, use the `-i` flag to make an interactive rebase, and then follow the instructions.**

```sh
git checkout <branch>  #which branch to rebase
git rebase <wheretorebase>  #where to
git push --force-with-lease #push the rebase
```

* Delete

```sh
git branch -d <name> #delete local branch
git branch -D <name> #force delete local branch
git push origin --delete <branch> #delete remote branch
```

## Tags

* Create a tag

```sh
git tag -a <name> -m "message"
git tag -a <name> <hash> #create a tag afterwards
```

* Handle remote tags

```sh
git push --tags
git tag -d <nametag> #delete it
```

## Debugging

* Dichotomy to find the error

```sh
git bisect start HEAD <hash>
# run the file to see if it works
git bisect <good/bad> #has the error ococured yet?
git bisect reset #HEAD goes back at the end
```

## Manipulate the graph of the worflow

* Squash n-last commits keeping the changes

**NB: Will require a `force-push` if commits already pushed!**

```sh
git reset --soft HEAD~ n && git commit -m "message"
```

* Choose some special commits with `cherry-picking`. The commit will be placed where the HEAD of the branch is.

```sh
git cherry-pick <commitA>
```

* See the log

```sh
git log --graph #show the full graph
git log --oneline --graph --color #readable graph
```