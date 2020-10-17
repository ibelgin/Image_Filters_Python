# Edge Enhance An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Emboss The Image
Edge_enhance = orginal.filter(ImageFilter.EDGE_ENHANCE) 
  
Edge_enhance.show() 
