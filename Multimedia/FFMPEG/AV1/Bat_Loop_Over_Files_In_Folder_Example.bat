Rem https://stackoverflow.com/questions/14237548/batch-script-run-command-on-each-file-in-directory
for /r %%v in (*.xls) do ssconvert "%%v" "%%vx"

Rem Example where the mp4 ending is also removed:
for /r %%v in (*.mp4) do ffmpeg -i "%%v" -c:v libsvtav1 -c:a libopus -ab 8k "%%~nv.webm" 

Rem Write each new file name to the terminal:
ECHO "%%~nv.webm"