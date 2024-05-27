#pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/mniet2009/tools_installation_scripts.git"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("maruti.svg", scale = 8) 
