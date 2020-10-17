# Brightness Enhancing
from PIL import Image, ImageEnhance
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
bightness = ImageEnhance.Brightness(orginal)
brightness.enhance(2.0).show()

