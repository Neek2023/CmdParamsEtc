sudo apt-get update && sudo apt-get upgrade

################################################################################
### https://averagelinuxuser.com/debian-11-after-install/
################################################################################
################################################################################
### If not already installed, install proper microcode:
################################################################################
sudo apt install intel-microcode

################################################################################
### Install build-essential
################################################################################
### It’s a package that includes many dependencies commonly used by different apps so it’s always good to have it installed. We all need it sooner or later.
sudo apt install build-essential dkms linux-headers-$(uname -r)

################################################################################
### install essential programs:
################################################################################
sudo apt-get install vim terminator vlc lshw htop flatpak 

################################################################################
### Install restricted-extras
################################################################################
sudo apt install libavcodec-extra gstreamer1.0-libav gstreamer1.0-plugins-ugly gstreamer1.0-vaapi firmware-iwlwifi

### Not found???????????????????????????????
 ttf-mscorefonts-installer
 rar
 unrar


################################################################################
### Microsoft Fonts Compatibility
################################################################################
sudo apt install fonts-crosextra-carlito fonts-crosextra-caladea

################################################################################
### Configure Swappiness
################################################################################
Check the current swappiness value by executing:
cat /proc/sys/vm/swappiness # 60 (default)
### bak config file:
sudo cp /etc/sysctl.conf /etc/sysctl.conf.bak
sudo vim /etc/sysctl.conf
### add to bottom to decrease swappiness (use the ram more and swap less)
vm.swappiness=10

################################################################################
### Speed up the Boot Time
################################################################################
### disable the GRUB screen and boot straight into Debian
sudo cp /etc/default/grub /etc/default/grub.bak
sudo vim /etc/default/grub
### set GRUB_TIMEOUT to 0 (instead of 5)
GRUB_TIMEOUT=0

# Update GRUB
sudo update-grub
### Note: If you happen to need a GRUB screen, you can still access it by pressing SHIFT on boot.


################################################################################
### Install Firewall
################################################################################
sudo apt install ufw
sudo ufw enable

################################################################################
### Install BackUp Program???????????????????????????????????????????
################################################################################
### BackUp programs are often overlooked. That is also the case with Debian 11 which doesn’t have backups by default. I always back up my system and good backups have saved me a few times!
### Timeshift is the gold standard for system backups in Linux. It’s also very easy to install and configure.

################################################################################
### Enable Snap and FlatPak in the software centre settings
################################################################################
### or do this: https://www.linuxcapable.com/how-to-install-flatpak-on-debian-linux/?utm_content=cmp-true
### Enable Flathub:
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
### To access and manage Flatpak applications via a graphical user interface (GUI), we will need to install GNOME Software. 
sudo apt install gnome-software-plugin-flatpak
### alternatively, it should just start working in the kde software app if kde is installed.
### another alternative, use command line:
flatpak search APP_NAME
flatpak install flathub APP_ID
### List Installed Flatpak Applications
flatpak list
### Update Flatpak Applications
flatpak update
### Remove Flatpak Applications
flatpak uninstall APP_ID


################################################################################
### Extend the Battery Life
################################################################################
### If you have Debian installed on your laptop, you can squeeze more battery juice by installing tlp (power management tool).
sudo apt install tlp

################################################################################
### terminator
################################################################################
### add terminator shortcut hotkeys to KDE settings (^+alt+t)

################################################################################
### Set-up wifi
################################################################################
### Save hardware profile into a html file for easier viewing:
sudo lshw -html > lshw.html
### search internet for:
debian install BCM43142 802.11b/g/n
### I discovered that the standard drivers do not cover this wireless card, but another, wl, does:
https://wiki.debian.org/wl
### Install wl:
### Need to install non-free compontents first:
### Add a "non-free" component to /etc/apt/sources.list for your Debian version, for example:
deb http://deb.debian.org/debian bookworm contrib non-free
deb-src http://deb.debian.org/debian bookworm contrib non-free
### Install the relevant/latest linux-image, linux-headers and broadcom-sta-dkms packages:
apt-get install linux-image-$(uname -r|sed 's,[^-]*-[^-]*-,,') linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,') broadcom-sta-dkms
### (Optional) Check all the built DKMS kernel modules. There should be "wl.ko" in the list.
find /lib/modules/$(uname -r)/updates
### Unload conflicting modules:
sudo modprobe -r b44 b43 b43legacy ssb brcmsmac bcma
### Load the wl module:
sudo modprobe wl


################################################################################
### Install DVD packages
################################################################################
### https://www.cyberciti.biz/faq/installing-plugins-codecs-libdvdcss-in-debian-ubuntu-linux/
sudo apt-get install libdvd-pkg
### download, compile, and install libdvdcss by typing the following dpkg-reconfigure command:
sudo dpkg-reconfigure libdvd-pkg
### install the regionset command, type:
sudo apt-get install regionset
"""
If your DVD player locks up when you try to playback a DVD, your DVD player probably does not match the DVD’s region code under DRM. Hence, we need to use the regionset command on your Linux machine as follows to set the correct region code for your DVD firmware:
sudo regionset /dev/sr0

As per the regionset man page:

There are eight region codes possible, currently six are used:

1 – North America (USA and Canada)
2 – Europe, Middle East, South Africa and Japan
3 – Southeast Asia, Taiwan, Korea
4 – Latin America, Australia, New Zealand
5 – Former Soviet Union (Russia, Ukraine, etc.), rest of Africa, India
6 – China
"""
sudo apt install dvdbackup libdvdnav-doc libdvdnav4 libdvdread8



################################################################################
### Install wine:
################################################################################
### You can identify your architecture with the following command:
dpkg --print-architecture
### E.g. for amd64 (which most users have) you may need i386. Enable it with the following command:
sudo dpkg --add-architecture i386 && sudo apt update
### install wine:
sudo apt install wine wine64 libwine fonts-wine wine32:i386
### To open the Wine configuration window, enter the following command:
winecfg
### To open the Wine registry editor, enter the following command:
regedit

### to install a program, launch the Windows installation file (.exe/.msi) with the following command:
wine setup.exe
### In order to remove a program, launch the wine uninstaller with the following command:
wine uninstaller




