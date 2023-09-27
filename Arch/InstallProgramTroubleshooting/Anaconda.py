################################################################################
### Anaconda Installation 2023-07-20 on ThinkPad x220 with Arch
################################################################################
### Anaconda is made to install on accounts you would normally not be able to install things on.
### Therefore, it is best to not install as sudo.
### Instead download the official installer bash script from the Anaconda website and run the installer on a normal account. 

### First install prerequisites:
pacman -Sy libxau libxi libxss libxtst libxcursor libxcomposite libxdamage libxfixes libxrandr libxrender mesa-libgl  alsa-lib libglvnd

### Then run the installer bash script
bash ~/Downloads/Anaconda3-2020.05-Linux-x86_64.sh

### Accept the license and accept the default install location (/home/userNameHere/anaconda3)

### Say yes to init conda
### Close and re-open your terminal window for the installation to take effect, or enter the command source ~/.bashrc to refresh the terminal.


### If you'd prefer that conda's base environment not be activated on startup, set the auto_activate_base parameter to false: 
conda config --set auto_activate_base false

################################################################################
### Get started with Anaconda Navigator
################################################################################
### First, activate conda environment using command:
conda activate

### Then launch Anaconda Navigator GUI:
anaconda-navigator
### The anaconda GUI should launch



### If working fine, proceed to the Anaconda text document in the Programing folder of this git repository for setting up the programing environment.




































































