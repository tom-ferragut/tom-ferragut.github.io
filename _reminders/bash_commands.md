---
title: Bash and other shell commands
---

Some shell commands that can be useful sometimes and keep spending too much time to find back.
For some commands I put the Windows equivalent (might be handy when not on your own machine).

## Regexp: everything seems easier after that

* General placements

```sh
^           #beginning of a line
$           #end of a line
*           #anything
```

* Occurrences for a character

```sh
x*         #x appears at least zero times
x+         #x appears at least once
x?         #x is facultative
x{4}       #a sequence of 4 x
x{2,4}     #x apppears 2, 3 or 4 times
\.         #match the . character
```

* Class of characters

```sh
[a-z]     #all lower cases letters
[Aa]bc    #abc with or without upper case for a
[^0-9]    #anything but numbers
```

* The alternative

```sh
mi[n|m]e  #match the words mime and mine
you|me|her #match any of the three
```

## Basics

* Move around

```sh
cd <path>  #go to <path>
cd ..      #go up in the tree structure
cd ~       #go home
cd         #go home
pwd        #print working directory
```

* Remove files (recursively)
**Be very careful with that one!**

```sh
rm -r
```

* Show files in a directory

```sh
ls
ls -a #show hidden files too
ls -l #show accesses and sizes
```

* Get help

```sh
man <fctn>
```

* Search commands

```sh
grep <regexp> <path>
```
The `-C` flags show the number of the lines, `-c` counts the number of lines, `-l` the name of the files containing the chain of characters.

```sh
find <path> <criteria> -print #find files matching the criteria
```
Some flags are `-name`, `-size` or `-mtime` (last modified).
To combine some criterions use `\(<match1> -o <match2>\)` it's the logical `or`.

```sh
ls -1 | wc -l #number of files in repository
```

* Create something new

```sh
mkir <name> #new repository
touch <name> #new empty file if doesn't exist
```
The `touch` command, when used on a pre-existing file, updates the time/date stamp.

* See the content

```sh
cat <file> #display the content
vi <file>  #open the default terminal editor, :q to exit
```

* Locate the executable (*eg* python...)

```sh
which <executable>
```

* Unzip folder

```sh
tar -xvf <file>.tar
tar zxvf <file>.tar.gz
unzip <file>.zip -d <directory>
```

With `unzip`, use `-o` to overwrite.


* Some Windows equivalents
For some commands, Unix and Windows are the same. Just try and/or Google it (especially don't try if it might be dangerous).

```sh
cd        #print working directory when on its own
deltree   #delete recursively
dir /ah   #show files
help      #get help
find      #equivalent of grep
tree | find <tomatch> #equivalent of unix find
edit      #equivalent of vi
where     #equivalent of which
```

## Environment variables

* Add one

```sh
export NAME=VALUE
```
This can be done in the shell, or in `~/.bashrc`.

* Reload the `.bashrc`

```sh
source ~/.bashrc
```

* See variables in `PATH`

```sh
echo $PATH
```

## Some SSH

* Send from local to remote

```sh
scp <path_to_file> <login>@<server>:<directory>
```
Use the `-r` flag for recursivity. If there is an error like `is a directory` it means it **isn't** a directory, so use `mkdir` and then try again.

* Send from remote to local

```sh
scp <login>@<server>:<path_to_file> <directory>
```
To transfer files, `rsync` is worth looking.

* Download from URL

```sh
wget <url>
```


## Time related

* Chronometer (when you don't have your phone at arms length)

```sh
date1=`date +%s`; while true; do echo -ne "$(date -u --date @$((`date +%s` - $date1)) +%H:%M:%S)\r"; done
```

* Display time

```sh
timedatectl #a lot of infos
date + "%d-%m-%y" #date with a format
date --date='23 Nov' +%u #which week day for my birthday?
```

* In Windows

```sh
date
time
```

## GPU related

* Info on the GPU hardware

```sh
lspci | grep -i --color 'vga\|3d\|2d'
```

* Cuda version and GPU status

```sh
nvidia-smi
```

## Visualize site locally

```sh
bundle-2.7 exec jekyll clean  #clean slate
bundle-2.7 exec jekyll serve  #make it available locally
```