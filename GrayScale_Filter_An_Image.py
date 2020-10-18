# GrayScale Filter An Image
from PIL import Image, ImageFilter 
  
# creating a image object 
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png") 
  
# Grayscale The Image
# Where "L" stands for 'luminous'.
grayscaled_Image = orginal.convert('L')
  
grayscaled_Image.show() 
