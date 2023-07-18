###############################################################################################################
###############################################################################################################
### Setup of new github repository:
###############################################################################################################
###############################################################################################################

### Make the new repository on github and add a README, license, etc. 

### https://stackoverflow.com/questions/1408790/how-do-i-pull-my-project-from-github
### First, you'll need to tell git about yourself. Get your username and token together from your settings page.
# https://github.com/settings/tokens

### Then run:
git config --global github.user YOUR_USERNAME
git config --global github.token YOURTOKEN

### You will need to generate a new (ed25519, not RSA anymore) key if you don't have a back-up of your key.
# http://help.github.com/msysgit-key-setup/
### Info about key phassphrases:
# https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases
### Add pub key to GitHub
# https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

### Then you should be able to run:

git clone git@github.com:YOUR_USERNAME/YOUR_PROJECT.git


###############################################################################################################
### https://github.com/git-guides/git-add
###############################################################################################################
### Use git add to stage file changes before making a commit
### Stage all files (that are not listed in the .gitignore) in the entire repository
git add .

### Stage a specific directory or file
git add <path>


###############################################################################################################
### https://github.com/git-guides/git-commit
###############################################################################################################
git commit: This starts the commit process, but since it doesn't include a -m flag for the message, your default text editor will be opened for you to create the commit message. If you haven't configured anything, there's a good chance this will be VI or Vim. (To get out, press esc, then :w, and then Enter.
git commit -m "descriptive commit message": This starts the commit process, and allows you to include the commit message at the same time.
git commit -am "descriptive commit message": In addition to including the commit message, this option allows you to skip the staging phase. The addition of -a will automatically stage any files that are already being tracked by Git (changes to files that you've committed before).


###############################################################################################################
### https://github.com/git-guides/git-push
###############################################################################################################
git push

### If key not saved and getting errors:
# eval "$(ssh-agent -s)"
# ssh-add ~/.ssh/id_ed25519_GitHub_Neek2023


###############################################################################################################
### https://github.com/git-guides/git-pull
###############################################################################################################
git pull

git fetch + git merge







