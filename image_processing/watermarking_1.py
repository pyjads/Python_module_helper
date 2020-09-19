#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np

#%%
watermark = cv2.imread(r"E:\Pycharm_Workspace\Data_Science\image_processing\watermark_1.jpg")
original_1 = cv2.imread(r'E:\Pycharm_Workspace\Data_Science\image_processing\original.jpg')

diff = watermark != original_1

print(diff.sum())

#%%

mark = 'E:\Pycharm_Workspace\Data_Science\image_processing\w_{}.jpg'

# im1 = mark.format('1')

w_1 = cv2.imread(mark.format('1'))
w_1 = np.array(w_1, dtype=np.uint16)

w_2 = cv2.imread(mark.format('2'))
w_2 = np.array(w_2, dtype=np.uint16)

w_3 = cv2.imread(mark.format('3'))
w_3 = np.array(w_3, dtype=np.uint16)

w_4 = cv2.imread(mark.format('4'))
w_4 = np.array(w_4, dtype=np.uint16)

w_5 = cv2.imread(mark.format('5'))
w_5 = np.array(w_5, dtype=np.uint16)

# average
final_image = (w_1 + w_2 + w_3 + w_4 + w_5)/5

cv2.imwrite('image_processing/image_average.jpg',final_image)


# majority

red = np.array([w_1.T[0],w_2.T[0], w_3.T[0], w_4.T[0], w_5.T[0]])
green = np.array([w_1.T[1],w_2.T[1], w_3.T[1], w_4.T[1], w_5.T[1]])
blue = np.array([w_1.T[2],w_2.T[2], w_3.T[2], w_4.T[2], w_5.T[2]])

red_majority = red.max(axis=0)
green_majority = green.max(axis=0)
blue_majority = blue.max(axis=0)

image_median = np.array([red_majority, green_majority, blue_majority])
cv2.imwrite('image_processing/image_median.jpg',final_image)


#%%
watermark = cv2.imread(r"E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_01.jpg")
original_1 = cv2.imread(r'E:\Pycharm_Workspace\Data_Science\image_processing\original.jpg')


print(original_1.shape)

#%%

watermark = cv2.imread(r"C:\Users\lenovo\Desktop\matlab\input_sat_image.jpg")
cv2.imshow('image',watermark)

#%%

from io import StringIO # "import StringIO" directly in python2
from PIL import Image
# im2 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork with OutGuess 02.jpg')
# im1 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_01.jpg')
# im3 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_03.jpg')
# im4 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_04.jpg')

im2 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\Test_OutGuess_01.jpg')
r, g, b = im2[:,:,0], im2[:,:,1], im2[:,:,2]
im2 = 0.2989 * r + 0.5870 * g + 0.1140 * b
im1 = Image.open('E:\Pycharm_Workspace\Data_Science\image_processing\Test_OutGuess_02.jpg')

im2.save('image_processing/1_c.jpg', quality=0)
im2.save('image_processing/2_c.jpg', quality=100)
im2.save('image_processing/3_c.jpg', quality=50)
im2.save('image_processing/4_c.jpg', quality=30)
im2.save('image_processing/5_c.jpg', quality=10)
# im3.save('image_processing/3_compressed.jpg', quality=0)
# im4.save('image_processing/4_compressed.jpg', quality=0)

#%%
im1 = cv2.imread('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork with OutGuess 02.jpg',0)
im2 = cv2.imread('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_01.jpg',0)
im3 = cv2.imread('E:\Pycharm_Workspace\Data_Science\image_processing\StegoWork_with_OutGuess_03.jpg',0)
plt.hist(im1.ravel(),256,[0,256], color='red')
plt.title('IM1')
plt.show()
plt.clf()
plt.hist(im2.ravel(),256,[0,256], color='green')
plt.title('IM2')
plt.show()
plt.clf()
plt.hist(im3.ravel(),256,[0,256], color='blue')
plt.title('IM3')
plt.show()



