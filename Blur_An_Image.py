# Blur An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Bluring The Image
blured_Image = orginal.filter(ImageFilter.BLUR) 
  
blured_Image.show() 
