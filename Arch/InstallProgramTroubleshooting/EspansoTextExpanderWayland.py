### espanso-wayland installed from the AUR:
### https://aur.archlinux.org/packages/espanso-wayland

### Register the service to systemd:
espanso service register

#(base) [neek@archX220 YtDLP]$ espanso service register
### command output:
#creating service file in "/home/neek/.config/systemd/user/espanso.service"
#enabling systemd service
#Created symlink /home/neek/.config/systemd/user/default.target.wants/espanso.service → /home/neek/.config/systemd/user/espanso.service.
#service registered correctly!


### running espanso start gave an error since it was already running:
espanso start
### command output:
#unable to start service: timed out
#Hint: sometimes this happens because another Espanso process is left running for some reason.
#      Please try running 'espanso restart' or manually killing all Espanso processes, then try again.
### Although the first time set-up window opened when I ran that


### Get keyboard layout:
localectl status
### Backup and update espanso .config file:
cp ~/.config/espanso/config/default.yml ~/.config/espanso/config/default.yml.bak
vim ~/.config/espanso/config/default.yml
### Append the following lines at the end of the file (assuming a gb layout keyboard:
keyboard_layout:
  { layout: gb }

### backup and edit base substitutions file:
cp ~/.config/espanso/match/base.yml ~/.config/espanso/match/base.yml.bak
vim ~/.config/espanso/match/base.yml


### Make your own match text files:
touch ~/.config/espanso/match/Example.yml

### Find espanso path on another system:
espanso path

###############################################################################
### Adding packages:
###############################################################################
### https://hub.espanso.org/math-symbols
espanso install math-symbols

### https://hub.espanso.org/all-emojis
espanso install all-emojis

### https://hub.espanso.org/greek-letters-improved
espanso install greek-letters-improved

### Can try later if one above not good enough
### https://hub.espanso.org/greek-letters-alt
# espanso install greek-letters-alt
### https://hub.espanso.org/greek-letters
# espanso install greek-letters

### https://hub.espanso.org/super-sub-scripts
espanso install super-sub-scripts

### https://hub.espanso.org/math
espanso install math

### Can try later
### https://hub.espanso.org/espanso-latex
# espanso install espanso-latex

### https://hub.espanso.org/italian-accents
espanso install italian-accents

### Can try later
### https://hub.espanso.org/italian-accented-words
# espanso install italian-accented-words



### You can uninstall a package with:
espanso uninstall <package_name>
### ou can also update all packages at once with:
espanso package update all

###Datetime scripting in base YML file:
  # Print the current date
  - trigger: "/date_"
    replace: "{{mydate}}"
    vars:
      - name: mydate
        type: date
        params:
          format: "%Y-%m-%d_"

  # Print the current date and time
  - trigger: "/datet_"
    replace: "{{mydate}}"
    vars:
      - name: mydate
        type: date
        params:
          format: "%Y-%m-%dT%H-%M_"

### sync between computers:
https://espanso.org/docs/sync/


