# Parameters:
#     size – Kernel size, given as (width, height). In the current version, this must be (3, 3) or (5, 5).
#     kernel – A sequence containing kernel weights.
#     scale – Scale factor. If given, the result for each pixel is divided by this value. the default is the sum of the kernel weights.
#     offset – Offset. If given, this value is added to the result, after it has been divided by the scale factor.

from PIL import Image, ImageFilter  
  
# creating a image object  
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png")  
  
# applying the Kernel filter 
kernal = orginal.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 11, -2, -2, -2, -2), 1, 0)) 
  
kernal = kernal.show()           
