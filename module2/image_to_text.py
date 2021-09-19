# selecting text by using easyOCR
import easyocr
import cv2

path = r'C:\Users\my-pc\Desktop\anaconda\hotu_data_scientist_resume\AdEase -ML-Task\web_page_scraping\images2\13.png'
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 

reader  = easyocr.Reader(['en'])
output = reader.readtext(path)         

output
print(output)


