# selecting text by using easyOCR
import easyocr
import cv2

image = cv2.imread('14.png')      #give the path of google ad
window_name = 'image'          
cv2.imshow('image',image)
  
cv2.waitKey(0)        #(this is necessary to avoid Python kernel form crashing)
cv2.destroyAllWindows()    #closing all open windows 

reader  = easyocr.Reader(['en'])
output = reader.readtext('14.png')          #give the path of google ad.

output
print(output)


