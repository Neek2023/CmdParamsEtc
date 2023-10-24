### Activating numlock on bootup
### https://wiki.archlinux.org/title/Activating_numlock_on_bootup#
### Early bootup (mkinitcpio)

yay -S mkinitcpio-numlock

### Edit /etc/mkinitcpio.conf:
cd /etc/
ls mkin*
sudo cp /etc/mkinitcpio.conf /etc/mkinitcpio.conf.bak
sudo vim /etc/mkinitcpio.conf

### add numlock to the following line as below (before encrypt if encryption is used)
HOOKS=(base udev autodetect keyboard keymap consolefont numlock modconf block encrypt lvm2 filesystems fsck)

### Then regenerate the initramfs for the change to take effect.
### Manual generation
### To run the script manually, refer to the mkinitcpio(8) manual page for instructions. In particular, to (re-)generate the preset provided by a kernel package, use the -p/--preset option followed by the preset to utilize. For example, for the linux package, use the command:
# mkinitcpio -p linux

### To (re-)generate all existing presets, use the -P/--allpresets switch. This is typically used to regenerate all the initramfs images after a change of the global #Configuration:
sudo mkinitcpio -P
### Users may create any number of initramfs images with a variety of different configurations. The desired image must be specified in the respective boot loader configuration file.


### could also try as a systemd service:
### https://wiki.archlinux.org/title/Activating_numlock_on_bootup#With_systemd_service



### Also in KDE:
### Go to System Settings > Input Devices > Keyboard, in the Hardware tab, in the NumLock on Plasma Startup section, choose the desired NumLock behavior.
