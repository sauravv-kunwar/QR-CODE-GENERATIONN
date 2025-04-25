import qrcode
from PIL import Image

# Create a QRCode object with specific configurations
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
#fill_color="cyan", back_color="black"

# Add data to the QR code
qr.add_data("Hey Babegirlllllllllll!!!!.png")
qr.make(fit=True)

# Generate the image with custom colors
img = qr.make_image(fill_color="cyan", back_color="black")

# Save the image with a proper extension
img.save("Made By Sauravvvvvv.png")
