###############################################################################
### Yay info
###############################################################################
### Yay commands are fairly similar to pacman commands for the most part. 


###############################################################################
### Install Yay
###############################################################################
### To install Yay on Arch Linux, first, download the following dependencies:
sudo pacman -S --needed base-devel git
 
### Then, clone the Yay repository using the git clone command:
git clone https://aur.archlinux.org/yay.git
 
### Change your present working directory to the newly-downloaded yay folder using the cd command:
cd yay
 
### Finally, use the makepkg command to build and install Yay:
makepkg -si
 
### Once done, verify the installation by checking the version of Yay installed:
yay --version
 



### Search for a package on both the official repositories and AUR, use the -Ss flag:
yay -Ss google-chrome
 
### to install packages:
yay -S packagename

### to remove a package from your system:
yay -R packagename
### If you want to remove the package along with its dependencies, append the -ns flag to the previous command:
yay -Rns google-chrome
 

### Upgrading AUR Packages
### Invoking the yay command without any arguments will perform a full system upgrade similar to the pacman -Syu command.
yay -Syu
### To only update AUR packages:
yay -Sua




### Using Yay to Remove Unnecessary Dependencies
### If not taken care of, unused dependencies can quickly pile up and consume a huge chunk of your system storage. You can either choose to remove the dependencies along with the packages by using the -Rns flag each time you remove something, or take the better route by sweeping them away all at once using the -Yc flag:
yay -Yc
### The -Y in the above command stands for "Yay" and will only perform operations on packages installed using Yay.


### To print package statistics and system health with Yay, run the following command:
yay -Ps

yay --help
man yay



### See yay stats:
yay -P --stats


