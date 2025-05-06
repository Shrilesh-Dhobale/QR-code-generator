import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)  
   #QRCode is fun use to change functionalities

qr.add_data("achievers01.netlify.app/courses")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="grey")
img.save("Achievers adv qr.png")
