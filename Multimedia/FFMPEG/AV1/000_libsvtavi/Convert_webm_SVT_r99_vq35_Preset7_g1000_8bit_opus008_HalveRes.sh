#!/bin/bash

for file in *.mov
do 
    echo "$file"
    ffmpeg -i "$file" -vf scale="iw/2:ih/2" -c:v libsvtav1 -crf 35 -preset 7 -g 1000 -c:a libopus -ab 8k "$file.webm"
done 



