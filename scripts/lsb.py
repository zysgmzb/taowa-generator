from PIL import Image
from io import BytesIO
from selectpic import selectpic

def lsb(secret_text: bytes) -> bytes:
    binary_secret_text = ''.join(format(data, '08b') for data in secret_text)
    res = selectpic(binary_secret_text)
    if(res):
        image = Image.open('./pics/' + res[1])
        binary_secret_text += '0' * res[0]
        secret_text_index = 0
        for y in range(image.height):
            for x in range(image.width):
                pixel = list(image.getpixel((x, y)))
                for i in range(3):
                    if secret_text_index < len(binary_secret_text):
                        pixel[i] = (pixel[i] & 0xFE) | int(binary_secret_text[secret_text_index])
                        secret_text_index += 1
                image.putpixel((x, y), tuple(pixel))

        output_image_io = BytesIO()
        image.save(output_image_io, format='PNG')
        return output_image_io.getvalue()
    else:
        return secret_text