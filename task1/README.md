# FFmpeg Conversion

### Install FFmpeg (For MacOS):
- A simple way to install FFmpeg for MAC OS
```
brew install ffmpeg
```

### Use FFmpeg to re-encode a video file (MOV, or MP4) to two bitrates:

- 720p at 2Mbps and 30fps
```
ffmpeg -i disney.MOV -c:a copy -c:v copy -r 30 -s hd720 -b:v 2M disney_30_720.MOV
```
- 480p at 1Mbps and 30fps
```
ffmpeg -i disney.MOV -c:a copy -c:v copy -r 30 -s hd480 -b:v 1M disney_30_480.MOV
```

### Insert Your Own API KEY
Insert your key @ tweets2image.py and grab tweets to the back ground image

### Convert Images to Video
- subprocess calls ffmpeg command
After getting the desired images:
```
python image2video.py
```
convert to video. Fps rate, etc can be set.

### Output
Output is called "out.mp4". One is copied from tweets folder.


