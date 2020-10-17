# Contour An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Contour The Image
Contour = orginal.filter(ImageFilter.CONTOUR) 
  
Contour.show() 
