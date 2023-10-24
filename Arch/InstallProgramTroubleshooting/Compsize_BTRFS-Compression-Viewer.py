### https://aur.archlinux.org/packages/compsize-git
### wait, there is compsize in pacman extra repository...
### https://superuser.com/questions/670125/how-do-i-find-out-the-compressed-uncompressed-file-sizes-on-btrfs

sudo Pacman -S compsize

### Usage example:
compsize /DIRECTORY/TREE/HERE

### Ex:
[~]$ compsize /home
Processed 140058 files, 133128 regular extents (196786 refs), 80886 inline.
Type       Perc     Disk Usage   Uncompressed Referenced
TOTAL       93%       14G          15G          12G
none       100%       13G          13G          10G
zlib        41%      628M         1.4G         1.4G
zstd        28%       42M         148M         148M
