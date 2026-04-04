#Completed by Yvonne Naa Ardua Anang,UNI: yna2103 with Joseph Duodu,UNI: jd3519
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


def rgb_ints_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3), dtype=np.uint8)
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 255
            # purple pixels
            # set all 3 color components
            img[x+50, y+50,:] = (128, 0, 128)
            # green pixels
            img[x+100,y+100,green] = 255
    return img

plt.imshow(rgb_ints_example())


def onechannel(pattern, rgb):
    new_pattern = np.copy(pattern)
    if rgb == 0:
        for x in range(new_pattern.shape[0]):
            for y in range(new_pattern.shape[1]):
                new_pattern[x, y, 1] = 0
                new_pattern[x, y, 2] = 0
        return new_pattern
    
    if rgb == 1:
        for x in range(new_pattern.shape[0]):
            for y in range(new_pattern.shape[1]):
                new_pattern[x, y, 0] = 0
                new_pattern[x, y, 2] = 0
        return new_pattern         
    
    if rgb == 2:
        for x in range(new_pattern.shape[0]):
            for y in range(new_pattern.shape[1]):
                new_pattern[x, y, 0] = 0
                new_pattern[x, y, 1] = 0
        return new_pattern  

def permutecolorchannels(img, perm):
    new_pattern = np.copy(img)
    for x in range(new_pattern.shape[0]):
        for y in range(new_pattern.shape[1]):
            for value in range(3):
                new_pattern[x, y, perm[value]] = img[x, y, value]
    return new_pattern


def decrypt(image, key):
    decrypted_image = np.copy(image)
    for i in range(3):
        for x in range(decrypted_image.shape[0]):
            decrypted_image[x,:,i] = decrypted_image[x,:,i]^key
    return decrypted_image

def main():
    if __name__ == "__main__":
        pattern = plt.imread("pattern.png")
        plt.imshow(onechannel(pattern, 0))
        plt.imshow(permutecolorchannels(pattern, [1, 0, 2]))
        
        permcolors = plt.imread("permcolors.jpg")
        plt.imshow(permutecolorchannels(permcolors, [1, 2, 0]))
        
        secret = plt.imread("secret.bmp")
        key = np.load("key.npy")
        plt.imshow(decrypt(secret, key))
        
main()



