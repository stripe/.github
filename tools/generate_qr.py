import qrcode

# رابط QR Code الخاص بالدفع
payment_link = "https://example.com/web-payments"

# توليد QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)
qr.add_data(payment_link)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("payment_qr.png")
