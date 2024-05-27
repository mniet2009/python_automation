#pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/@CURRENT_INSTRUMENTATION_CANADA"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("anand.svg", scale = 8) 
