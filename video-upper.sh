ffmpeg -framerate 24 -start_number 0 -i upper/%03d.png -r 30 -an -vcodec libx264 -pix_fmt yuv420p upper.mp4
