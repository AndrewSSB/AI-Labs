import numpy as np
from skimage import io

images:np.array = []
for i in range(0, 9):
    images.append(np.load(f"images\\car_{i}.npy"))

#b)
sum = 0
for image in images:
    sum = +np.sum(image)

print(sum)



#c)
sum_parte = []
suma_max = np.sum(images[0])
index = 0

for i in range(len(images)):
    sum_parte.append(np.sum(images[i]))
    if np.sum(images[i]) > suma_max:
        suma_max = np.sum(images[i])
        index = i
#d)

print(index)

#e)

mean_img = np.mean(images, axis=0)
io.imshow(mean_img.astype(np.uint8))
io.show()


#f)

std_img = np.std(images)
print(std_img)

#g)
for i in range(len(images)):
    images[i] = images[i] - mean_img
    np.divide(images[i], std_img)
    io.imshow(images[i].astype(np.uint8))
    io.show()
#h)
for i in range(len(images)):
    pic = images[i][200:301, 280:401]
    io.imshow(pic.astype(np.uint8))
    io.show()