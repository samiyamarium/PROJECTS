import qrcode

data = "Don't forget to subscribe"

# Create QRCode object
qr = qrcode.QRCode(
    version=1,         # Controls the size of the QR code
    box_size=10,       # Size of each box in pixels
    border=5           # Thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

# Create image with color customization
img = qr.make_image(fill_color='red', back_color='black')

# Save the image (Windows path should be raw string or double backslashes)
img.save("C:/Users/Haier/Desktop/python practice/assignment01/03_qrcode/qr.png")

#print(img)
