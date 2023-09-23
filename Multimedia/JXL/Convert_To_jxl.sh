#!/bin/bash

for file in *.jpg
do 
    echo "$file"
    #cjxl --lossless_jpeg=0 --quality=50 --effort=9 "$file" "$file.jxl"
    magick "$file" -resize 50% "$file.2.jpg"
    cjxl --lossless_jpeg=0 --quality=50 --effort=9 "$file.2.jpg" "$file.jxl"
done 



