### https://github.com/yt-dlp/yt-dlp
### https://github.com/yt-dlp/yt-dlp#format-selection-examples
### https://wiki.archlinux.org/title/Yt-dlp
### https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
### https://itsfoss.com/youtube-dl-gui-apps/
### tartube gui??? https://aur.archlinux.org/packages/tartube

###############################################################################
### Normal Usage Commands
###############################################################################
### List video and audio formats:
yt-dlp -F URL

### DL worst webm with height>=720 and worst webm audio with tbr>50
yt-dlp -f "wv*[ext=webm][height>=?720]+wa*[ext=webm][tbr>?50]" URL

### DL video format 247 and audio format 250
yt-dlp -f 247+250 URL




###############################################################################
### Subtitles
###############################################################################
### To see which languages are available:
yt-dlp --list-subs URL

### To download a video with selected subtitles (comma separated):
yt-dlp --write-sub --sub-lang LANG URL

### For auto-generated subtitles:
yt-dlp --write-auto-sub --sub-lang LANG URL
### Add --skip-download to get only subtitles.


###############################################################################
### Faster downloads
###############################################################################
### Some websites throttle transfer speeds. You can often get around this by choosing non DASH streams or by using aria2, an external downloader which supports multi-connection downloads. For example:
yt-dlp --external-downloader aria2c --external-downloader-args '-c -j 3 -x 3 -s 3 -k 1M' URL


###############################################################################
### Playlist
###############################################################################
### Using youtube-dl for a playlist usually boils down to the following options:
yt-dlp --ignore-errors --continue --no-overwrites --download-archive progress.txt usual options URL
### This set of options allow for the download to effectively continue even after interruption. If you are archiving, add the usual --write-xxx and --embed-xxx options you may have.


###############################################################################
### Trim (partial download)
###############################################################################
### Parts of videos can be downloaded by using the output of yt-dlp -g -f format URL as ffmpeg input with the -ss (for input), -t and -c copy options.


###############################################################################
### URL from clipboard
###############################################################################
### A shell alias, a desktop launcher or a keyboard shortcut can be set to download a video (or audio) of a selected (or copied) URL by outputting it from the X selection. See Clipboard#Tools.

yt-dlp -f "wv*[ext=webm][height>=?720]+wa*[ext=webm][tbr>?50]" --write-auto-sub --sub-lang en --limit-rate 1M URL

#--playlist-start NUMBER          Playlist video to start at (default is 1)
#--playlist-end NUMBER            Playlist video to end at (default is last)






