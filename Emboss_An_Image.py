# EMBOSS An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Emboss The Image
Emboss = orginal.filter(ImageFilter.EMBOSS) 
  
Emboss.show() 
