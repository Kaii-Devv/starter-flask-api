from PIL import Image
import io

# Membuka gambar
with open('/storage/emulated/0/WhatsApp/Media/WhatsApp Images/IMG-20240305-WA0001.jpg', 'rb') as file:
    img_bytes = file.read()

# Membuat objek Image dari bytes
image = Image.open(io.BytesIO(img_bytes))
print(io.BytesIO(img_bytes))
# Menampilkan gambar di Chrome
image.show()
