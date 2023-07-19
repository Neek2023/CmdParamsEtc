###############################################################################
### Zoom
################################################################################
### 2023-07-19 Zoom builds fine but crashes when a sidebar loads when opening. The fix is to change an environment variable, close the sidebar, and then change the environment variable back. 

### How to set an environment variable
### https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/
### To set an environment variable
export NAME=VALUE
### We give the variable a name, which is what is used to access it in shell scripts and configurations and then a value to hold whatever data is needed in the variable.


### Ex.
### start zoom after changing the following environment variable: 
export QT_QPA_PLATFORM=xcb
### Toggle off the Zoom sidebar. After that change the environment variable back to the following and run zoom. 
export QT_QPA_PLATFORM=wayland
### and it will not crash untill you toggle the sidebar back














































































