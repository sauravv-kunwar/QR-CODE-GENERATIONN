import qrcode
from PIL import Image

# QR Code configuration
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow logo overlay
    box_size=10,
    border=4
)

# Add data
qr.add_data("https://github.com/sauravv-kunwar")
qr.make(fit=True)

# Create base QR image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo image
logo = Image.open("github_logo.png")  

# Resize the logo
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.25)  # logo will be 25% the size of the QR
logo = logo.resize((logo_size, logo_size))

# Calculate position to center the logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste logo into QR code
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Save final image
qr_img.save("sauravv_github_with_logo.png")
