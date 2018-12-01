# Zad 2 Przekształć wczytane obrazki w opisany sposób
# numpy.ipynb

import matplotlib.pyplot as plt
%matplotlib inline

import matplotlib.image as mpimg
im1 = mpimg.imread('szablony_cwiczen/images/monkey.png')

# stwórz wycinek - spróbuj wybrać twarz
plt.imshow(im1[35:160, 100:170])

# wybierz jeden kolor
## first
im1.shape
plt.imshow(im1[:,:,1])
plt.imshow(im1*np.array([True, True, False, 1]))
## next second
red = True
green = False
blue=False
alpha=1
mask = np.array([red,green,blue,alpha])
plt.imshow(im1*mask)


# Obrót o wskazaną liczbę stopni
### pip install scipy
from scipy import ndimage
plt.show(ndimage.rotate(im1, 45))


# Czarno biały filtr
### 1
im1[:,:,1] = im1[:,:,0]
im1[:,:,2] = im1[:,:,0]
plt.imshow(im1)

### 2
suma_z_warstw = im1.sum(axis=2, keepdims=True)
# suma_z_warstw = suma_z_warstw / 3 jak wynik jest za duzy to obrazek jest biały
suma_z_warstw = suma_z_warstw / np.max(suma_z_warstw)
# suma_z_warstw.shape
data = np.ones(3) * suma_z_warstw
# data.shape
plt.imshow(data)

# Rozmazanie
ndimage.gaussian_filter?
plt.imshow(ndimage.gaussian_filter(im1, 3))