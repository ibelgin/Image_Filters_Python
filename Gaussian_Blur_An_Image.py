# Gaussian Blur An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Gaussian Blur An Image
Blur = orginal.filter(ImageFilter.GaussianBlur(radius = 5))

Blur.show() 
