### Trying to create a test environment:
conda create -n testEnv python spyder
conda env list
### My new env appeared :-)

conda activate testEnv
### testEnv is now activated

conda search numpy
conda install numpy
### looks ok so far

(testEnv) [neek@archX220 ~]$ anaconda-navigator
bash: anaconda-navigator: command not found
### uh oh, can't use anaconda-navigator when not in base???
### Switching to base:
(testEnv) [neek@archX220 ~]$ conda activate base
(base) [neek@archX220 ~]$ anaconda-navigator
### anaconda-navigator opens fine. when I switch to testEnv, I see Spyder is installed and it seems to open fine!

conda install -c conda-forge opencv
conda install -c conda-forge python-docx
conda install -c conda-forge imageio
conda install -c conda-forge matplotlib
conda install -c conda-forge pypdf2
conda install -c conda-forge selenium

conda install -c anaconda spyder
conda install -c anaconda pandas
conda install -c anaconda scipy
conda install -c anaconda jupyter

### Again but more all together in fewer lines:
# conda install -c anaconda sypder pandas scipy juptyer #this line does not seem to work
conda install -c conda-forge opencv python-docx imageio matplotlib pypdf2 selenium


### https://stackoverflow.com/questions/72166020/how-to-install-multiple-packages-in-one-line-using-conda
### The recommended way to install multiple packages is to create a .yml file and feed conda this. You can specify the version number for each package as well.


### Packages to check:
### See test script that tries to import all these to see which need to still be installed
### The install commands above should install all of the below
bs4
ctypes
cv2
datetime
docx
enum
imageio
math
matplotlib
numpy
os
pandas
pprint
PyPDF2
random
re
requests
selenium
scipy
statistics
time
urllib.parse

#packages not found:
copy
csv


################################################################################
### yml file package installation (all at once)
################################################################################
### https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
### You can create an environment file (environment.yml) manually to share with others. Example:
name: stats2
channels:
  - javascript
dependencies:
  - python=3.9
  - bokeh=2.4.2
  - conda-forge::numpy=1.21.*
  - nodejs=16.13.*
  - flask
  - pip
  - pip:
    - Flask-Testing



### To install packages from a yml file, use:
conda env update -n my_env --file ENV.yaml


### My first attempt at this:
conda create -n GeneralScienceEnv
conda env update -n GeneralScienceEnv --file GenScience.yml
### This takes a while on the ThinkPad x220 computer...and then FREEZES the computer...
### So I gave up on this way for now...I may try to install all packages in a testEnvironemnt and save a yml file from that one to re-use instead of trying to build a yml file manually...


### I just removed the previous version of this environment and restarted it this way:
conda create -n GeneralScienceEnv python spyder jupyter pandas scipy
conda activate GeneralScienceEnv
conda install -c conda-forge opencv python-docx imageio matplotlib pypdf2 selenium
### Just tested GeneralScienceEnv in Spyder and it seems to load all my imported modules in my test .py script. 

### In the future, consider trying mamba instead of conda:
### https://stackoverflow.com/questions/63734508/stuck-at-solving-environment-on-anaconda
### https://github.com/mamba-org/mamba

























