# Convert images grabbed from twitter to video
import os
import subprocess

os.chdir('tweets/')
# -r is the framerate (fps)
# -crf is the quality, lower means better quality, 15-25 is usually good
# -s is the resolution
# -pix_fmt yuv420p specifies the pixel format, change this as needed
subprocess.call(['ffmpeg','-r','1/3','-f', 'image2','-s','1920x1080','-i', 'img%d.png', '-vcodec','libx264','-crf','25', '-pix_fmt','yuv420p','out.mp4'])