# Box Blur An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Box Blur An Image
Box_Blur = orginal.filter(ImageFilter.BoxBlur(8)) 
# 8 is the radius the size of the box in one direction
  
Box_Blur.show() 
