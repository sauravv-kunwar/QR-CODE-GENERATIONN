import qrcode
from PIL import Image

# Create a QRCode object with specific configurations
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("https://www.linkedin.com/in/saurav-kunwar-98a632340/")
qr.make(fit=True)

# Generate the image with a cool color combo
img = qr.make_image(fill_color="blue", back_color="#FFFFF0")  # ForestGreen on Ivory

# Save the image
img.save("saurav_linkedin.png")
