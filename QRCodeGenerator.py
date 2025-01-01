import qrcode


qr =qrcode.QRCode(
    version =1, #version of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #size of the QR box
    border=5 #white part of the border
)

data ="https://www.linkedin.com/in/sevmim/"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")