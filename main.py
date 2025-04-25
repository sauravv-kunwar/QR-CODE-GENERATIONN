# firstly you have to install pip install qrcode
import qrcode as qr
img = qr.make("https://github.com/sauravv-kunwar")
img.save("saurav_github.png")
