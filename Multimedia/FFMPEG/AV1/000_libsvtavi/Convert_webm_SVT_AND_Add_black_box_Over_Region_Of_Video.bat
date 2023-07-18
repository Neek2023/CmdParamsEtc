for /r %%v in (*.webm) do ffmpeg -i "%%v" -c:v libsvtav1 -r 5 -crf 35 -preset 7 -g 1000 -vf "drawbox=x=1550:y=135:w=500:h=900:color=black@0.7:t=fill" -c:a libopus -ab 8k "%%~nv.2.webm" 
Rem ECHO "%%v.webm"



Rem Draw a black box over the right side area of the screen:
Rem -vf "color=black:400x900 [over]; [in][over] overlay=1585:135 [out]"
Rem https://stackoverflow.com/questions/11503997/put-a-black-box-image-over-existing-video-using-ffmpeg
Rem ffmpeg.exe -i in -vf "color=black:20x10 [over]; [in][over] overlay=5:5 [out]" out
Rem Replacing 20x10 and 5:5 with the width x height of the box and the position of the timestamp as necessary.
Rem OR
Rem https://superuser.com/questions/1221633/ffmpeg-setting-a-rectangle-in-a-video-to-black
Rem -vf "drawbox=x=10:y=10:w=100:h=100:color=pink@0.5:t=fill"