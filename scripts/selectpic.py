from PIL import Image
import numpy as np
import os

def selectpic(secret_text: bytes) -> str:
    secret_len = len(secret_text)
    all_image = np.array(os.listdir('./pics'))
    all_pixels = np.sort(np.vectorize(lambda s: int(s[:-4]))(all_image))
    for i in all_pixels:
        if(secret_len <= i):
            return i - secret_len, str(i) + '.png'
        return None
