### https://www.dwarmstrong.org/btrfs-snapshots-rollbacks/
### https://wiki.archlinux.org/title/Snapper
### https://github.com/wesbarnett/snap-pac
### https://archlinux.org/packages/extra/any/snap-pac/
### https://wiki.archlinux.org/title/Pacman/Tips_and_tricks
### Deeper BRTFS reference:
### https://wiki.archlinux.org/title/Btrfs#Snapshots
###############################################################################
### Set up automatic snapshots of a BTRFS root subvolume, add these snapshots to the GRUB boot menu, and gain the ability to rollback an Arch Linux system to an earlier state.
###############################################################################

### In prev. tutorial (https://www.dwarmstrong.org/archlinux-install/), the author created:
###     @ subvolume, mounted to /. Create snapshots of this root subvolume.
###     @snapshots and other subvolumes, which are excluded from root snapshots.
"""
###_I create additional subvolumes for more fine-grained control over rolling back the system to a previous state, while preserving the current state of other directories. These subvolumes will be excluded from any root subvolume snapshots:
###_Subvolume -- Mountpoint:

@home -- /home (preserve user data)
@snapshots -- /.snapshots
@cache -- /var/cache
@libvirt -- /var/lib/libvirt (virtual machine images)
@log -- /var/log (excluding log files makes troubleshooting easier after reverting /)
@tmp -- /var/tmp


###_The subvolume creation commangs:
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@snapshots
btrfs subvolume create /mnt/@cache
btrfs subvolume create /mnt/@libvirt
btrfs subvolume create /mnt/@log
btrfs subvolume create /mnt/@tmp

###_Unmount the root partition ...
umount /mnt

###_Set mount options for the subvolumes ...
export sv_opts="rw,noatime,compress-force=zstd:1,space_cache=v2"
###_options:
    ###_noatime increases performance and reduces SSD writes.
    ###_compress-force=zstd:1 is optimal for NVME devices. Omit the :1 to use the default level of 3. Zstd accepts a value range of 1-15, with higher levels trading speed and memory for higher compression ratios.
    ###_space_cache=v2 creates cache in memory for greatly improved performance.

###_Mount the new BTRFS root subvolume with subvol=@
mount -o ${sv_opts},subvol=@ /dev/mapper/cryptdev /mnt

###_Create mountpoints for the additional subvolumes:
mkdir -p /mnt/{home,.snapshots,var/cache,var/lib/libvirt,var/log,var/tmp}

###_Mount the additional subvolumes:
mount -o ${sv_opts},subvol=@home /dev/mapper/cryptdev /mnt/home
mount -o ${sv_opts},subvol=@snapshots /dev/mapper/cryptdev /mnt/.snapshots
mount -o ${sv_opts},subvol=@cache /dev/mapper/cryptdev /mnt/var/cache
mount -o ${sv_opts},subvol=@libvirt /dev/mapper/cryptdev /mnt/var/lib/libvirt
mount -o ${sv_opts},subvol=@log /dev/mapper/cryptdev /mnt/var/log
mount -o ${sv_opts},subvol=@tmp /dev/mapper/cryptdev /mnt/var/tmp
...
"""

###----------------------------------------------------------------------------
### Install Snapper and snap-pac:
###----------------------------------------------------------------------------
sudo pacman -S snapper snap-pac

### Additionally, GUIs are available with snapper-gui-git AUR and btrfs-assistant AUR.
yay -S snapper-gui-git btrfs-assistant

### Note this warning during installation:
"""
(1/2) installing snapper-gui-git                                                         [###################################################] 100%
warning: directory permissions differ on /home/neek/
filesystem: 700  package: 755
>>>
>>> You must create a default config with snapper cli named root first.
>>> Run 'snapper -c root create-config /' as root
>>>
"""

### optional packages to install for these:
sudo pacman -S kdesu btrfsmaintenance

###############################################################################
### Create snapshot configuration for root subvolume
###############################################################################
### Snapper's create-config command assumes:
    ### Subvolume @ already exists and is mounted at /.
    ### /.snapshots directory is not mounted and doesn't exist.
### During my Arch install, I created the @ and @snapshots subvolumes, and /.snapshots mountpoint. Before letting Snapper do its config thing, I need to move my earlier snapshot setup out of the way.

### Unmount the subvolume and remove the mountpoint:
sudo umount /.snapshots
sudo rm -rf /.snapshots

### Create a new snapper configuration named config for the Btrfs subvolume at /path/to/subvolume:
#sudo snapper -c config create-config /path/to/subvolume
### Create a new root config:
sudo snapper -c root create-config /
### This generates:
    ### Configuration file at /etc/snapper/configs/root.
    ### Add root to SNAPPER_CONFIGS in /etc/conf.d/snapper.
    ### Subvolume .snapshots where future snapshots for this configuration will be stored.

### Note: eventually I should consider making another snapper configuration for my home directory?????????????????????????????????????????????????????????????????????????

###############################################################################
### Setup /.snapshots
###############################################################################
### List subvolumes:
sudo btrfs subvolume list /
"""
ID 256 gen 199 top level 5 path @
ID 257 gen 186 top level 5 path @home
ID 258 gen 9 top level 5 path @snapshots
[...]
ID 265 gen 199 top level 256 path .snapshots
"""
### Note the @snapshots BTRFS subvolume I had created earlier, and the .snapshots BTRFS subvolume created by Snapper.
### I prefer my @snapshots BRTFS subvolume setup over .snapshots BRTFS subvolume, so I delete the Snapper-generated subvolume ...
sudo btrfs subvolume delete .snapshots
### command terminal output:
#Delete subvolume (no-commit): '//.snapshots'

### Re-create and re-mount /.snapshots mountpoint:
sudo mkdir /.snapshots
sudo mount -a

### This setup will make all snapshots created by Snapper be stored outside of the @ subvolume. This allows replacing @ without losing the snapshots.
### Set permissions. Owner must be root, and I allow members of wheel to browse through snapshots ...
sudo chmod 750 /.snapshots
sudo chown :wheel /.snapshots

###############################################################################
### Manual snapshot
###############################################################################
### Example of taking a manual snapshot of a fresh install ...
sudo snapper -c root create -d "**Base system install**"

###############################################################################
### Automatic timeline snapshots
###############################################################################
### Setup timed auto-snapshots by modifying /etc/snapper/configs/root.

### Allow user (example: foo) to work with snapshots:
#ALLOW_USERS="foo"
ALLOW_USERS="neek"

### Example: Set some timed snapshot limits:
"""
TIMELINE_MIN_AGE="1800"
TIMELINE_LIMIT_HOURLY="5"
TIMELINE_LIMIT_DAILY="7"
TIMELINE_LIMIT_WEEKLY="0"
TIMELINE_LIMIT_MONTHLY="0"
TIMELINE_LIMIT_YEARLY="0"
"""

### Start and enable snapper-timeline.timer to launch the automatic snapshot timeline, and snapper-cleanup.timer to periodically clean up older snapshots:
sudo systemctl enable --now snapper-timeline.timer
sudo systemctl enable --now snapper-cleanup.timer


###############################################################################
### Pacman snapshots
###############################################################################
### Pacman pre- and post- snapshots are triggered before and after a significant change (such as a system update).
### Example: I install the program tree (to test snapper), which triggers a pre and post install snapshot.
### List configs:
snapper list-configs
"""
Config | Subvolume
-------+----------
root   | /
"""

### List snapshots taken for root:
snapper -c root list
"""
 # | Type   | Pre # | Date                        | User | Cleanup  | Description             | Userdata
---+--------+-------+-----------------------------+------+----------+-------------------------+---------
0  | single |       |                             | root |          | current                 |
1  | single |       | Sat 20 Aug 2022 11:21:53 AM | root |          | **Base system install** |
2  | pre    |       | Sat 20 Aug 2022 11:22:39 AM | root | number   | pacman -S tree          |
3  | post   |     2 | Sat 20 Aug 2022 11:22:39 AM | root | number   | tree                    |
4  | single |       | Sat 20 Aug 2022 12:00:04 PM | root | timeline | timeline                |
"""

### List updated subvolumes list, which now includes the snapshots:
sudo btrfs subvolume list /
"""
ID 256 gen 270 top level 5 path @
ID 257 gen 270 top level 5 path @home
ID 258 gen 257 top level 5 path @snapshots
[...]
ID 266 gen 216 top level 258 path @snapshots/1/snapshot
ID 267 gen 218 top level 258 path @snapshots/2/snapshot
ID 268 gen 219 top level 258 path @snapshots/3/snapshot
ID 269 gen 237 top level 258 path @snapshots/4/snapshot
"""

###############################################################################
### Updatedb
###############################################################################
### If locate is installed, skip indexing .snapshots directory by adding to /etc/updatedb.conf:
PRUNENAMES = ".snapshots"
### 2023-10-01_ I did not have locate installed, so I did not do this. Do it later if locate is added!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





###############################################################################
### NOTE: I skipped the Grub instructions below for now as I do not see why I would want them at the moment. Need to do later if I want more than arch iso recovery option????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
### skip this section on directions on how to manually reset to a snapshot (writable home directory) A.K.A. do a "rollback""
###############################################################################
### Grub-btrfs
###############################################################################
### Include the snapshots as boot options in the GRUB boot loader menu.
### Install:
sudo pacman -S grub-btrfs

### Set the location of the directory containing the grub.cfg file in /etc/default/grub-btrfs/config.
### Example: My grub.cfg is located in /efi/grub
GRUB_BTRFS_GRUB_DIRNAME="/efi/grub"


###############################################################################
### Auto-update GRUB
###############################################################################
### Enable grub-btrfs.path to auto-regenerate grub-btrfs.cfg whenever a modification appears in /.snapshots:
sudo systemctl enable --now grub-btrfs.path

### At the next boot, there is an submenu in GRUB for Arch Linux snapshots.


###############################################################################
### Read-only snapshots and overlayfs
###############################################################################
### Booting on a snapshot is done in read-only mode.
### This can be tricky:
### An elegant way is to boot this snapshot using overlayfs ... Using overlayfs, the booted snapshot will behave like a live-cd in non-persistent mode. The snapshot will not be modified, the system will be able to boot correctly, because a writeable folder will be included in the RAM ... Any changes in this system thus started will be lost when the system is rebooted/shutdown.
### Add the hook grub-btrfs-overlayfs at the end of HOOKS in /etc/mkinitcpio.conf:
HOOKS=(base ... fsck grub-btrfs-overlayfs)

### Re-generate initramfs ...
sudo mkinitcpio -P
### Note: Any snapshots that do not include this modified initramfs will not be able to use overlayfs.







###############################################################################
### System rollback the 'Arch Way'
###############################################################################
### Snapper includes a rollback tool, but on Arch systems the preferred method is a manual rollback.
### After booting into a snapshot mounted rw courtesy of overlayfs, mount the toplevel subvolume (subvolid=5). That is, omit any subvolid or subvol mount flags (example: an encrypted device map labelled cryptdev):
sudo mount /dev/mapper/cryptdev /mnt

### Move the broken @ subvolume out of the way:
sudo mv /mnt/@ /mnt/@.broken

### Or simply delete the subvolume:
sudo btrfs subvolume delete /mnt/@

### Find the number of the snapshot that you want to recover:
sudo grep -r '<date>' /mnt/@snapshots/*/info.xml
"""
[...]
/.snapshots/8/info.xml:  <date>2022-08-20 15:21:53</date>
/.snapshots/9/info.xml:  <date>2022-08-20 15:22:39</date>
"""

### Create a read-write snapshot of the read-only snapshot taken by Snapper:
sudo btrfs subvolume snapshot /mnt/@snapshots/number/snapshot /mnt/@

### Where number is the snapshot you wish to restore as the new @.
Unmount /mnt.

### Reboot and rollback!
### Alternatively, consider installing snapper-rollback from yay to automate the process:
### https://aur.archlinux.org/packages/snapper-rollback
### https://github.com/jrabinow/snapper-rollback




### Next make sure that non-BTRFS partitions (e.g. /boot) is also backed up:
### https://wiki.archlinux.org/title/System_backup#Snapshots_and_/boot_partition
### This is nice for backing up before kernal updates

### Snapshots and /boot partition # https://wiki.archlinux.org/title/System_backup#Snapshots_and_/boot_partition
### If your file system supports snapshots (e.g., LVM or Btrfs), these will most likely exclude the /boot partition or ESP.
### You can copy the boot partition automatically on a kernel update to your root partition with a pacman hook (make sure the hook file is owned by root):

### vim /etc/pacman.d/hooks/95-bootbackup.hook #note this directory would need to be created and activated
### Instead of the above hook file, make the hook file in this directory:
cd /usr/share/libalpm/hooks/
sudo touch 95-bootbackup.hook
"""
[Trigger]
Operation = Upgrade
Operation = Install
Operation = Remove
Type = Path
Target = usr/lib/modules/*/vmlinuzls


[Action]
Depends = rsync
Description = Backing up /boot...
When = PostTransaction
Exec = /usr/bin/rsync -a --delete /boot /.bootbackup
"""







