for /r %%v in (*.mp4) do ffmpeg  -i "%%v" -c:v libaom-av1 -strict experimental -r 10 -crf 35 -cpu-used 4 -row-mt 1 -tile-columns 2 -tile-rows 1 -g 1000 -c:a libopus -ab 8k "%%~nv.webm" 
Rem ECHO "%%v.webm"


