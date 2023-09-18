import random
import pyzipper
import os
import io

def weakpasszip(secret_text: bytes) -> bytes:
    dictionary = open('./dicts/weak.txt').readlines()
    dict_len = len(dictionary) - 2
    password = dictionary[random.randint(0, dict_len)].strip()

    zip_data = io.BytesIO()

    with pyzipper.AESZipFile(zip_data, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_ref:
        zip_ref.setpassword(password.encode())
        zip_ref.writestr(bytes.hex(os.urandom(5)), secret_text)

    zip_data.seek(0)

    return zip_data.getvalue()