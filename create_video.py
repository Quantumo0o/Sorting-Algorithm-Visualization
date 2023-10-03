import cv2
import os

# Get the current working directory
current_directory = os.getcwd()

# Sort the image filenames numerically
image_files1 = [filename for filename in os.listdir(current_directory) if filename.endswith('.jpg')]

image_files = sorted(image_files1, key=lambda x: os.path.getmtime(x), reverse=False)


# Specify the video output file and codec
video_name = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, 1, (2000, 1000))  # Adjust width and height as needed

# Combine the images into a video
for image_file in image_files:
    img = cv2.imread(image_file)
    video.write(img)

# Release the video object
video.release()
