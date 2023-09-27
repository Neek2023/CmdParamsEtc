### make the following directory and file if not there already:
~/.config/terminator/
touch ~/.config/terminator/config

### if the file is already there, then make a backup of it:
cp ~/.config/terminator/config ~/.config/terminator/config.bak

### edit the file as below:
vim ~/.config/terminator/config

### config looks something like this originally:
"""
[global_config]
[keybindings]
[layouts]
  [[default]]
    [[[child1]]]
      parent = window0
      profile = default
      type = Terminal
    [[[window0]]]
      parent = ""
      type = Window
      size = 1200, 700
[plugins]

"""
### Add or adjust size = WWWW, HHH under [[[window0]]]

### Also change the color scheme
### Right click background of terminator screen
### Select Preferences
### Go to Profiles tab
### Go to Colors subtab
### Select "White on black" from "Built-in schemes"

