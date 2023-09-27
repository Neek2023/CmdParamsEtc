### Guide sources: 
### https://www.howtogeek.com/766168/how-to-install-arch-linux-on-a-pc/
### https://itsfoss.com/install-arch-linux/
### or https://itsfoss.com/install-arch-linux-virtualbox/ for virtualbox archinstall script
### https://itsfoss.com/btrfs/


##############################################################################################################################
### Manage ISO file
##############################################################################################################################
### download iso
https://archlinux.org/download/
https://geo.mirror.pkgbuild.com/iso/

### write iso to usb disc
dd bs=4M if=/path/to/archlinux.iso of=/dev/sdx status=progress && sync
### Plug in usb and boot computer with usb drive.


##############################################################################################################################
### If desired, use archinstall script instead of all the things below
##############################################################################################################################
archinstall



##############################################################################################################################
### Preliminary Steps - Setup netowrking and time sync
##############################################################################################################################
### check networking if plugged in
ping google.com

### if failed, 
### check the name of your wireless interface by issuing the device list command. Generally, the name of the wireless interface will start with a “w”,  such as wlan0 or wlp2s0.
iwctl device list

### establish an internet connection using the iwctl command
### Next, run the following commands to scan for your SSID and connect to it. Replace [device] and [SSID] in the commands with your wireless interface and Wi-Fi name respectively.
iwctl station [device] get-networks
iwctl station [device] connect [SSID]
### The system will then ask you for the Wi-Fi password if you have one set up. Type it in and press “Enter” to continue. Run ping google.com again to verify the connection.


### Enable network time synchronization using timedatectl:
timedatectl set-ntp true


pacman -S vim


### Select an appropriate mirror (Might need to do later in the order of things after setting up partitions?????????????????????????????????????????????
### First sync the pacman repository so that you can download and install software:
pacman -Syy

### install reflector too that you can use to list the fresh and fast mirrors located in your country:
pacman -S reflector


### Make a backup of mirror list (just in case):
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak

### Now, get the good mirror list with reflector and save it to mirrorlist. You can change the country from US to your own country.
reflector -c "US" -f 12 -l 10 -n 12 --save /etc/pacman.d/mirrorlist



##############################################################################################################################
### keyboards
##############################################################################################################################
### If you face difficulty, you can list out all the supported keyboard layout:
ls /usr/share/kbd/keymaps/**/*.map.gz
### And then change the layout to the an appropriate one using loadkeys command. For example, if you want a German keyboard, this is what you’ll use:
loadkeys de-latin1



##############################################################################################################################
### Install the Arch Linux System
##############################################################################################################################
###===========================================================================================================================
### Creating the Necessary Partitions
###===========================================================================================================================
### Create three partitions: 
### - EFI
### - root
### - swap
### List the available storage devices on your system using fdisk -l. 
fdisk -l
### Most of the time, the HDD would be listed as /dev/sda and SSDs will be listed as /dev/nvme0n1


### Check if you have UEFI mode enabled
# Some steps are different for UEFI and non-UEFI systems. Use this command:
ls /sys/firmware/efi/efivars
### If this directory exists, you have a UEFI enabled system. You should follow the steps for UEFI system. 
### The steps that differ are clearly mentioned.



###Install BTRFS progs
pacman -S btrfs-progs



### First, select the disk you are going to format and partition:


### Run fdisk  by typing fdisk /dev/sda or fdisk /dev/nvme0n1, depending on whether you’re installing the OS on an HDD or SSD. 
#fdisk /dev/sda #For HDD
fdisk /dev/nvme0n1 #For SSD
### I suggest that you delete any existing partitions on the disk using command d. #2023-09-23_did not seem to do anyhing for me???
### Then, type g and hit “Enter” to create a new GPT partition table.

### Type n to create a new EFI partition and choose the partition type primary . 
### Hit “Enter” twice to proceed with the default partition number and first sector value.
### For the partition size, you can either enter the sector number manually or specify the size you want the partition to have. Since you don’t want to waste disk space on EFI partitions, any number between 500M and 1G would work. 
### Type +550M and press “Enter” to continue. (Or replace 550M in the command with the size you want for the partition.)

#### Alternate/additional step in fdisk?: (https://itsfoss.com/install-arch-linux/)
#### One important steps is to change the type of the EFI partition to EFI System (instead of Linux system).
#### Enter t to change type. Enter L to see all the partition types available and then enter its corresponding number to the EFI system.


### Similarly, create a swap partition with +2G as the last sector value. 

### Create a root partition and allocate all the remaining sectors to it by simply continuing with the default configurations.

### By default, all the partitions will have the “Linux Filesystem” type. To change this, type t and hit “Enter” to proceed. Select the EFI partition by entering 1 . Then, type ef to change the filesystem to EFI System type.

### Similarly, select the swap partition (partition number 2) and type 82 to convert the partition type to Linux swap. The root partition should be of Linux filesystem type, so we don’t need to change it.

### Type w and hit “Enter” to write the changes to the disk.


###---------------------------------------------------------------------------------------------------------------------------
### Formatting the Partitions (for UEFI system)
###---------------------------------------------------------------------------------------------------------------------------
### Format the /dev/sda1 (EFI) partition to FAT32 by typing:
mkfs.fat -F32 /dev/sda1 #only for sata, etc.
#if neded view partitions with:
lsblk
#if using ssd instead, format efi partition with:
mkfs.fat -F32 /dev/nvme0n1p1

### Instructions for EXT4 (also consider LVM...)
###  format the /dev/sda3 (root) partition to ext4:
mkfs.ext4 /dev/sda3

### Issue the following commands one by one to format and enable the swap partition:
mkswap /dev/sda2
swapon /dev/sda2

### Warning: For those who are dual-booting Linux with Windows, make sure you have the correct partitions set up. Pay extra attention when you’re formatting partitions or creating new ones, as a mistake here can render your Windows system useless.


###---------------------------------------------------------------------------------------------------------------------------
### Alternate instructions for btrfs
###---------------------------------------------------------------------------------------------------------------------------
### https://wiki.archlinux.org/title/Btrfs#Preparation
### Create a Btrfs filesystem on partition /dev/partition:
#mkfs.btrfs -L mylabel /dev/partition
mkfs.btrfs -L arch /dev/nvme0n1p2

###---------------------------------------------------------------------------------------------------------------------------
### Mounting (With Compression)
###---------------------------------------------------------------------------------------------------------------------------
### Btrfs supports transparent and automatic compression. This reduces the size of files as well as significantly increases the lifespan of flash-based media by reducing write amplification...
### Better performance is generally achieved with the fastest compress algorithms, zstd and lzo
### The compress=alg[:level] mount option enables automatically considering every file for compression, where alg is either zlib, lzo, zstd, or no (for no compression). Using this option, btrfs will check if compressing the first portion of the data shrinks it. If it does, the entire write to that file will be compressed. If it does not, none of it is compressed. 
### To enable compression when installing Arch to an empty Btrfs partition, use the compress option when mounting the file system: 
#mount -o compress=zstd[:level] /dev/sdxY /mnt/
mount -o compress=zstd:1 /dev/nvme0n1p2 /mnt/
### (Can leave out the "-o compress..." if no comresppsion wanted)
### During configuration, add compress=zstd to the mount options of the root file system in fstab.
### View compression types and ratios
### compsize takes a list of files (or an entire btrfs filesystem) and measures compression types used and effective compression ratios. 
### https://archlinux.org/packages/?name=compsize

### If messedup:
umount /mnt
### Then re-mount


###---------------------------------------------------------------------------------------------------------------------------
### Subvolumes
###---------------------------------------------------------------------------------------------------------------------------
### Creating a subvolume
### To create a subvolume, the btrfs filesystem must be mounted. The subvolume's name is set using the last argument.
btrfs subvolume create /path/to/subvolume

### Listing subvolumes
### To see a list of current subvolumes and their ids under path:
btrfs subvolume list -p path
###Deleting a subvolume
### To delete a subvolume:
btrfs subvolume delete /path/to/subvolume
### Alternatively, a subvolume can be deleted like a regular directory (rm -r, rmdir).

### Mounting subvolumes
### Subvolumes can be mounted like file system partitions using the subvol=/path/to/subvolume or subvolid=objectid mount flags. ...

### Create subvolumes compatible with snapper:
cd /mnt
btrfs subvolume create @
btrfs subvolume create @home
btrfs subvolume create @snapshots
btrfs subvolume create @var_log
btrfs subvolume create @swap

### Mount the subvolumes:
### https://www.codyhou.com/arch-encrypt-swap/
### https://github.com/Deebble/arch-btrfs-install-guide
### https://github.com/egara/arch-btrfs-installation
cd
umount /mnt
mount -o compress=zstd:1,subvol=@ /dev/nvme0n1p2 /mnt
mkdir -p /mnt/{boot,home,.snapshots,var/log,swap}
mount -o compress=zstd:1,subvol=@home /dev/nvme0n1p2 /mnt/home
mount -o compress=zstd:1,subvol=@snapshots /dev/nvme0n1p2 /mnt/.snapshots
mount -o compress=zstd:1,subvol=@var_log /dev/nvme0n1p2 /mnt/var/log
mount -o subvol=@swap /dev/nvme0n1p2 /mnt/swap

### Make sure swap subvolume is not being snapshotted??????????????????????????????
###, then create a swap file (my rule of thumb is 2 GB for VMs or 0.5 times the system RAM in GB????????; change count= parameter to your swap file size, in MB) and turn it on.
### https://wiki.archlinux.org/title/Swap#Swap_file_creation
cd /mnt/swap
chattr +C /mnt/swap   #this disables CoW
### Use dd to create a swap file the size of your choosing. For example, creating an 8 GiB swap file:
#dd if=/dev/zero of=./swapfile bs=1M count=8k status=progress
dd if=/dev/zero of=./swapfile bs=1M count=4k status=progress
chmod 0600 ./swapfile #owner read write
### After creating the correctly sized file, format it to swap:
mkswap -U clear ./swapfile
### Activate the swap file:
swapon ./swapfile

### All BTRFS pages I had open at this point:
### https://wiki.archlinux.org/title/Btrfs#Subvolumes
### https://duckduckgo.com/?q=create+btrfs+arch&t=brave&ia=web
### https://github.com/Deebble/arch-btrfs-install-guide
### https://github.com/egara/arch-btrfs-installation
### https://www.codyhou.com/arch-encrypt-swap/
### https://wiki.archlinux.org/title/Swap
### https://wiki.archlinux.org/title/Btrfs#Swap_file
### https://wiki.archlinux.org/title/Swap#Swap_file_creation

###Swap file removal if ever desired
###To remove a swap file, it must be turned off first and then can be removed:
swapoff /swapfile
rm -f /swapfile
### Finally, remove the relevant entry from /etc/fstab.

### Swappiness:
### https://wiki.archlinux.org/title/Swap#Swappiness



###---------------------------------------------------------------------------------------------------------------------------
### Creating filesystem for non-UEFI system
###---------------------------------------------------------------------------------------------------------------------------
### For non-UEFI system, you only have one single root partition. So just make it ext4:
mkfs.ext4 /dev/sda1




###===========================================================================================================================
### Installing and Configuring the System
###===========================================================================================================================
### To be able to install Arch on your disk, you need to mount the created partitions to appropriate directories. Mount the root partition ( /dev/sda3 ) to the /mnt directory.
mount /dev/sda3 /mnt
### or
mount /dev/nvme0n1p1 /mnt/boot

### install the base Linux packages to the mounted root partition.
pacstrap /mnt base base-devel linux linux-firmware intel-ucode vim sudo git btrfs-progs exfat-utils ntfs-3g man-pages man-db texinfo
### maybe add -K flag???
### This will take some time depending on your network connection.

### Generate a file system table using the genfstab command.
genfstab -U /mnt >> /mnt/etc/fstab
### The Arch Linux system is up and running on the /mnt directory.

### You can change root to access the new system by typing:
arch-chroot /mnt
### The change in the bash prompt denotes that you’ve now logged in to the newly installed Arch Linux system. Before you can proceed further, you’ll have to configure some settings and install the necessary packages for the system to work properly.

### Set the local timezone by creating a symlink between the “/usr/share/zoneinfo” and “/etc/localtime” directories.
#ln -sf /usr/share/zoneinfo/Region/City /etc/localtime #generic version of the command
#ln -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime
ln -sf /usr/share/zoneinfo/Europe/London /etc/localtime
### Replace the “Region” and “City” in the above command with the appropriate timezone. You can refer to this timezone database to check the region and city you need to input.
### https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
### America/Los_Angeles
### America/Chicago
### America/New_York
### Europe/London
### Europe/Rome

### sync the hardware clock with the system time
hwclock --systohc

### install Vim (or another text editor of your choice) and the “networkmanager” package.
pacman -S vim networkmanager

### edit the “/etc/locale.gen” file using your text editor and uncomment the locale statement that suits your needs. 
vim /etc/locale.gen
### For US, uncomment the en_US.UTF-8 UTF-8 line in the file using Vim.
### For UK, uncomment en_GB.UTF-8
#****************************************************
### save the file

### Generate the locale configuration.
locale-gen
### add following steps for non-default US??? https://itsfoss.com/install-arch-linux/
#echo LANG=en_GB.UTF-8 > /etc/locale.conf
#export LANG=en_GB.UTF-8

###Create the locale.conf(5) file, and set the LANG variable accordingly in /etc/locale.conf
LANG=en_US.UTF-8
###If you set the console keyboard layout, make the changes persistent in vconsole.conf(5) in /etc/vconsole.conf
#KEYMAP=de-latin1




### create a new hostname file inside /etc and add the hostname you want for your computer in the file. 
vim /etc/hostname
### This can be anything you want, and you don’t need to enter anything but the name. 
### When done, save the file.

### https://wiki.archlinux.org/title/Network_configuration ??????? Maybe look at more later...

### Create another text file with the name hosts under the /etc directory.
vim /etc/hosts
### You’ll notice that the file already contains some comments. Leave the comments as is.
### append the following text to the file. 
127.0.0.1        localhost
::1              localhost
127.0.1.1        hostname.localdomain        hostname
### *** (Remember to replace hostname in the command with the system hostname you set in the previous step). ***



###===========================================================================================================================
### Creating and Configuring Users
###===========================================================================================================================
### Set up the root user password by typing the passwd command. 
passwd
### Then, create an additional non-root user using useradd as follows, replacing username with your username:
useradd -m username
### *** replace username with your username ***

### Configure the new user’s password using the passwd command, again replacing username with your username.
passwd username

### Add the new user to the groups wheel , audio , and video using the command given below. Replace username with your username, and note that the group names in the command don’t have spaces after the commas.
usermod -aG wheel,video,audio username
### ***username***



###===========================================================================================================================
### Setting Up the GRUB Bootloader for the UEFI systems
###===========================================================================================================================
### install the grub package using pacman.
### https://wiki.archlinux.org/title/GRUB
pacman -S grub

### install these additional packages required for the bootloader to work properly.
pacman -S efibootmgr dosfstools os-prober mtools


### mount /dev/nvme0n1p1 /mnt/boot

### Mount your EFI partition ( /dev/sda1 ) to the /boot/EFI directory. 
mkdir /boot/EFI

mount /dev/sda1 /boot/EFI
#or
mount /dev/nvme0n1p1 /boot/EFI
###Note that you’ll have to create the directory first with mkdir .

### run the grub-install script to install the bootloader in the EFI directory.
grub-install --target=x86_64-efi --efi-directory=/boot/EFI --bootloader-id=grub

### Generate a GRUB configuration file
grub-mkconfig -o /boot/grub/grub.cfg




###===========================================================================================================================
### Setting Up the GRUB Bootloader for the non-UEFI systems
###===========================================================================================================================
### install grub package first:
pacman -S grub

### And then install grub like this (don’t put the disk number sda1, just the disk name sda):
grub-install /dev/sda

###Last step:
grub-mkconfig -o /boot/grub/grub.cfg



### reboot and remove the install medium
### reset wireless network settings...I had trouble with this, so I remounted the partitions from usb iso and arch-chrooted back in...
### Maybe do this before reboot: Install iwd or wpa_supplicant. Typical rant: wifi was working during installation and now it's not.
### https://wiki.archlinux.org/title/Network_configuration



###===========================================================================================================================
### Install a Desktop Environment in Arch
###===========================================================================================================================
### You can install whichever DE you prefer, but we will install the KDE Plasma desktop on this system. 
### Before that, however, let’s configure the display server, network manager, and similar services.
### install the xorg , plasma-meta , and kde-applications packages:
pacman -S xorg wayland wayland-docs
pacman -S plasma-meta kde-applications plasma-wayland-session

### if selecting pipewire-jack and wireplumber, then also run:
pacman -S pipewire-alsa pipewire-pulse


### Then, enable the SDDM and NetworkManager services 
systemctl enable sddm
systemctl enable NetworkManager

### if using a HiDPI display, follow this directions to scale sddm to screen resolution:
### https://wiki.archlinux.org/title/SDDM#Enable_HiDPI
### Create the following file:
sudo touch /etc/sddm.conf.d/hidpi.conf
sudo vim /etc/sddm.conf.d/hidpi.conf
### enter the following:
[Wayland]
EnableHiDPI=true

[X11]
EnableHiDPI=true

### When using Wayland, the HiDPI scaling depends on the greeter used.[3] For instance, when using a Qt-based greeter such as Breeze, add the following configuration:
[General]
GreeterEnvironment=QT_SCREEN_SCALE_FACTORS=2,QT_FONT_DPI=192


### Exit the arch-chroot environment by typing exit. 
exit

### unmount the root partition mounted in the /mnt directory
umount -f /mnt

###  restart your system by typing reboot 
#reboot
sudo shutdown -h now
### remove the installation media

### Once the system boots, you’ll notice that the dark terminal screen is now replaced with the colorful SDDM splash screen.
### To log in, type the user password and hit “Enter.” 
### You can also install multiple desktop environments and switch between each using the “Session” dropdown menu in the splash screen.







https://itsfoss.com/things-to-do-after-installing-arch-linux/
### Update your system
sudo pacman -Syu

### 1. Installing X server, Desktop Environment and Display Manager
sudo pacman -S xorg

### To install GNOME:
sudo pacman -S gnome gnome-extra
### To install Cinnamon:
sudo pacman -S cinnamon nemo-fileroller
### To install XFCE:
sudo pacman -S xfce4 xfce4-goodies
### To install KDE:
sudo pacman -S plasma
### To install MATE:
sudo pacman -S mate mate-extra

### You will also need a display manager to log in to your desktop environment. For the ease, you can install LXDM.
pacman -S lxdm
### Once installed, you can enable to start each time you reboot your system.
systemctl enable lxdm.service
### Reboot your system and you will see the LXDM login screen, select your desktop environment from the list and login.



###2. Install an LTS kernel
###Why should you install LTS kernel in Arch Linux when it is supposed to be cutting edge?

### Installing an LTS kernel means you have a more stable kernel with better support to older hardware. Also, the LTS kernels are supported for at least 2 years with bug fixes and performance enhancements.

###If you rather choose to use the latest Linux kernel, you may find regression and bugs introduced by the latest kernel updates to your existing software and system. It’s not a certainty but it is definitely a possibility. For example, a Kernel update broke GNOME in Arch based Linux some time back.

### This is why it is advisable to use an LTS kernel if you prefer a more stable system and/or have an older one. But the decision is yours to make.

### Before you install an LTS kernel, check the Linux kernel version you are using.
uname -r

### To install the LTS kernel and Linux LTS headers, type the below command:
sudo pacman -S linux-lts linux-lts-headers
# At this point, the LTS version is the default one.
### update the grub config:
grub-mkconfig -o /boot/grub/grub.cfg
### reboot the computer

#Once done, you can remove the older kernels by typing the below command. However, I prefer to keep it in “case” something goes wrong, I can boot into the other Linux kernel version.
sudo pacman -Rs linux




### 5. Installing Codecs and plugins
### Type the below command in the terminal:
sudo pacman -S a52dec faac faad2 flac jasper lame libdca libdv libmad libmpeg2 libtheora libvorbis libxv wavpack x264 xvidcore gstreamer0.10-plugins
### However, installing a media player like VLC imports all the necessary codecs and installs it.
sudo pacman -S vlc
### You may add a music player too:
sudo pacman -S amarok


### 6. Installing productive software
### For day to day use and setting up your Arch system for productive use, you need some basic applications like an office suite, email client, a web browser etc.
sudo pacman -S libreoffice thunderbird firefox gedit flashplugin skype dropbox aria2
### Aria2 is a download manager, LibreOffice is the most popular open source office suite, Thunderbird is a cross-platform mail and chat client, Firefox is an open source and free web browser, Gedit is an editor, flashplugin installs flash, Skype is a popular messaging and video calling software and Dropbox – to store your file for anytime access.
### Along with these, you will need archive managers
sudo pacman -S p7zip p7zip-plugins unrar tar rsync



### Disable GRUB delay
### To speed up your boot process, you can disable the GRUB screen that shows GRUB menu with 5-sec countdown and start booting right away. If you ever need the GRUB menu, you can call it by holding the Esc key during boot.
### To enable this functionality, first open the GRUB config:
sudo vim /etc/default/grub
### Add or change the line where this variable is:
set GRUB_TIMEOUT_STYLE=hidden.

### Update the GRUB config:
sudo grub-mkconfig -o /boot/grub/grub.cfg
### Reboot and your system will boot 5 second faster.


### set up periodic SSD trim:
sudo systemctl enable fstrim.timer
### The fstrim service will write to syslog every time it's invoked:
journalctl -u fstrim
### Ex output:
# Feb 07 19:18:23 fstrim[401]: /: 484.5 GiB (520173604864 bytes) trimmed on /dev/sdb3



### Additional tip:
### At any point in time, if you feel like removing any application (and its dependencies), you can use these commands:
sudo pacman -R package-name
### It removes the package without removing the dependencies. If you want to remove the dependencies but leaving out the ones which are being used by some other application, below command will help:
sudo pacman -Rs package-name
