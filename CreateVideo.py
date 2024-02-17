import os
import cv2

path = "C:\Users\sponnapa\Desktop\Lasya\Pro-C117\Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splittext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imreead(images[0])
frame.shape = height, width, channels
size = (width,height)
print(size)

out = cv2VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

print("Done")

