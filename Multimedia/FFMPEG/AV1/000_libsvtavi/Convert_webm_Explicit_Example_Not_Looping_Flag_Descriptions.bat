Rem General ffmpeg command structure:
ffmpeg  -i input.mp4 -c:v libsvtav1 -crf 35 -present 7 -g 1000 -pix_fmt yuv420p10le -c:a libopus -ab 8k output.webm

Rem ffmpeg -i Input.mp4 -c:v copy -t 00:36:00 -c:a copy Output.mp4