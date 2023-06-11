import os
import cv2

path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = os.path.join(path, file)
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

if count > 0:
    frame = cv2.imread(images[0])
    if frame is not None:
        height, width, channels = frame.shape
        size = (width, height)
        print(size)

        out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

        for i in range(0, count):
            frame = cv2.imread(images[i])
            out.write(frame)

        out.release()
        print("done")
    else:
        print("Failed to read the first image file.")
else:
    print("No image files found in the specified directory.")
