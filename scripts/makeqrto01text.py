from io import BytesIO
from PIL import Image
import qrcode

def makeqrto01text(secret_text: bytes) -> bytes:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=1,
        border=1,
    )
    try:
        qr.add_data(secret_text)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        stream = BytesIO()
        image.save(stream, format="PNG")
        image = Image.open(stream)
        pixel = ''
        for y in range(image.height):
            for x in range(image.width):
                pixel += str((image.getpixel((x, y)) + 1) % 2)

        return pixel.encode()
    except:
        return secret_text