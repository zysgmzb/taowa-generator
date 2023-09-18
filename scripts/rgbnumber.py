from PIL import Image
from io import BytesIO
import math

def rgbnumber(secret_text: bytes) -> bytes:
    secret_len = len(secret_text)
    sqrt = int(math.sqrt(secret_len / 3) + 1)
    image = Image.new('RGB', (sqrt, sqrt))
    secret_text += b'\x00' * (sqrt * sqrt * 3 - secret_len)
    secret_index = 0
    for y in range(sqrt):
        for x in range(sqrt):
            image.putpixel((x, y), (secret_text[secret_index], secret_text[secret_index + 1], secret_text[secret_index + 2]))
            secret_index += 3

    output_image_io = BytesIO()
    image.save(output_image_io, format='PNG')

    return output_image_io.getvalue()