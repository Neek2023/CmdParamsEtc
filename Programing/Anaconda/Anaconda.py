################################################################################
### Anaconda commands, etc. First written on Arch x220 on 2023-07-20
################################################################################

################################################################################
### Managing conda
################################################################################
### https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-conda.html
### To verify that conda is installed, in your terminal window or an Anaconda Prompt, run:
conda --version

### To update conda, in your terminal window or an Anaconda Prompt, run:
conda update conda


################################################################################
### List environments and packages
################################################################################

### To see a list of all of your environments, in your terminal window or an Anaconda Prompt, run:
conda info --envs
### OR
conda env list

### To see a list of all packages installed in a specific environment:
### If the environment is not activated, in your terminal window or an Anaconda Prompt, run:
conda list -n myenv

### If the environment is activated, in your terminal window or an Anaconda Prompt, run:
conda list

### To see if a specific package is installed in an environment, in your terminal window or an Anaconda Prompt, run:
conda list -n myenv scipy

###--------------------------------------------------------------------------------
### Create environment
###--------------------------------------------------------------------------------
### To create an environment with a specific package:
#conda create -n myenv scipy
### Tip: Install all the programs that you want in this environment at the same time. Installing 1 program at a time can lead to dependency conflicts.
conda create -n ScienceGeneralEnv python rstudio-desktop spyder

### Spyder, Jupyter notebooks, RStudio
### To install this package run one of the following:
# conda install -c r rstudio
### https://stackoverflow.com/questions/58923166/installing-r-studio-with-anaconda
### Basically all Rtudio via conda are out of date!
### To install this package run one of the following:
# conda install -c anaconda spyder


### activate environment
conda activate ENVNAME



### Sharing an environment
### You may want to share your environment with someone else---for example, so they can re-create a test that you have done. To allow them to quickly reproduce your environment, with all of its packages and versions, give them a copy of your environment.yml file.


### To remove an environment, in your terminal window or an Anaconda Prompt, run:
conda remove --name myenv --all
### You may instead use conda env remove --name myenv.
### To verify that the environment was removed, in your terminal window or an Anaconda Prompt, run:
conda info --envs
### The environments list that displays should not show the removed environment.


###--------------------------------------------------------------------------------
### pip
###--------------------------------------------------------------------------------
### To use pip in your environment, in your terminal window or an Anaconda Prompt, run:
conda install -n myenv pip
conda activate myenv
pip <pip_subcommand>
### Issues may arise when using pip and conda together. When combining conda and pip, it is best to use an isolated conda environment. Only after conda has been used to install as many packages as possible should pip be used to install any remaining software. If modifications are needed to the environment, it is best to create a new environment rather than running conda after pip. When appropriate, conda and pip requirements should be stored in text files.


################################################################################
### Channels (Package sources)
################################################################################
### Conda channels are the locations where packages are stored. They serve as the base for hosting and managing packages. Conda packages are downloaded from remote channels, which are URLs to directories containing conda packages. The conda command searches a default set of channels and packages are automatically downloaded and updated from the default channel. Read more about conda channels and the various terms of service for their use.
### Different channels can have the same package, so conda must handle these channel collisions.

### The following command adds the channel "new_channel" to the top of the channel list, making it the highest priority:
conda config --add channels new_channel

### Conda has an equivalent command:
conda config --prepend channels new_channel

### Conda also has a command that adds the new channel to the bottom of the channel list, making it the lowest priority:
conda config --append channels new_channel


################################################################################
### Packages
################################################################################
### To see if a specific package, such as SciPy, is available for installation:
conda search scipy

### To see if a specific package, such as SciPy, is available for installation from Anaconda.org:
conda search --override-channels --channel defaults scipy

### To see if a specific package, such as iminuit, exists in a specific channel, such as http://conda.anaconda.org/mutirri, and is available for installation:
conda search --override-channels --channel http://conda.anaconda.org/mutirri iminuit


### To install a specific package such as SciPy into an existing environment "myenv":
conda install --name myenv scipy

### If you do not specify the environment name, which in this example is done by --name myenv, the package installs into the current environment:
conda install scipy

### To install a specific version of a package such as SciPy:
conda install scipy=0.15.0

### To install multiple packages at once, such as SciPy and cURL:
conda install scipy curl

### TIP: It is best to install all packages at once, so that all of the dependencies are installed at the same time.


### To remove a package such as SciPy in an environment such as myenv:
conda remove -n myenv scipy

### To remove a package such as SciPy in the current environment:
conda remove scipy



###-----------------------------------------------------------------------------
### Installing packages from yml file
###-----------------------------------------------------------------------------
conda env update -n my_env --file ENV.yml
### THIS IS THE PREFERED WAY TO INSTALL A LOT OF PACKAGES AT ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



###-----------------------------------------------------------------------------
### Installing packages from Anaconda.org
###-----------------------------------------------------------------------------
### Packages that are not available using conda install can be obtained from Anaconda.org, a package management service for both public and private package repositories. Anaconda.org is an Anaconda product, just like Anaconda and Miniconda.

### To install a package from Anaconda.org:
### In a browser, go to http://anaconda.org.
### To find the package named bottleneck, type bottleneck in the top-left box named Search Packages.
### Find the package that you want and click it to go to the detail page.
### The detail page displays the name of the channel. In this example it is the "pandas" channel.
### Now that you know the channel name, use the conda install command to install the package. In your terminal window or an Anaconda Prompt, run:
conda install -c pandas bottleneck
### This command tells conda to install the bottleneck package from the pandas channel on Anaconda.org.

### To check that the package is installed, in your terminal window or an Anaconda Prompt, run:
conda list
### A list of packages appears, including bottleneck.


###-----------------------------------------------------------------------------
### Installing non-conda packages
###-----------------------------------------------------------------------------
### If a package is not available from conda or Anaconda.org, you may be able to find and install the package via conda-forge or with another package manager like pip.
### Pip packages do not have all the features of conda packages and we recommend first trying to install any package with conda. If the package is unavailable through conda, try finding and installing it with conda-forge.
### If you still cannot install the package, you can try installing it with pip. The differences between pip and conda packages cause certain unavoidable limits in compatibility but conda works hard to be as compatible with pip as possible.
### Note: Both pip and conda are included in Anaconda and Miniconda, so you do not need to install them separately.
### Conda environments replace virtualenv, so there is no need to activate a virtualenv before using pip.
### It is possible to have pip installed outside a conda environment or inside a conda environment.
### To gain the benefits of conda integration, be sure to install pip inside the currently active conda environment and then install packages with that instance of pip. The command conda list shows packages installed this way, with a label showing that they were installed with pip.
### You can install pip in the current conda environment with the command conda install pip, as discussed in Using pip in an environment.
### If there are instances of pip installed both inside and outside the current conda environment, the instance of pip installed inside the current conda environment is used.
### To install a non-conda package:
### Activate the environment where you want to put the program:
### On Windows, in your Anaconda Prompt, run activate myenv.
### On macOS and Linux, in your terminal window, run conda activate myenv.
### To use pip to install a program such as See, in your terminal window or an Anaconda Prompt, run:
pip install see
### To verify the package was installed, in your terminal window or an Anaconda Prompt, run:
conda list
### If the package is not shown, install pip as described in Using pip in an environment and try these commands again.


################################################################################
### Managing Python
################################################################################
### Installing PyPy
### To use the PyPy builds you can do the following:
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n pypy pypy
conda activate pypy



################################################################################
### Mamba package manager
################################################################################
### Consider installing Mamba package manager since it's written in C++ and suposedly a lot faster
### https://stackoverflow.com/questions/63734508/stuck-at-solving-environment-on-anaconda
### https://github.com/mamba-org/mamba

### install mamba
conda install -n base conda-forge::mamba

### use mamba
mamba install -c selenium
### https://linuxcommandlibrary.com/man/mamba











































