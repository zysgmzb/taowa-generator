from PIL import Image
import os

def pretreatment() -> None:
    all_image = os.listdir('./pics')
    for i in all_image:
        image = Image.open('./pics/' + i)
        pixels = image.width * image.height * 3
        if(i != str(pixels) + '.png' or image.mode != 'RGB'):
            image = image.convert("RGB")
            image.save('./pics/' + str(pixels) + '.png', format='PNG')
            os.remove('./pics/' + i)