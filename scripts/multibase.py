from base64 import b32encode as base32
from base64 import b64encode as base64
from base64 import b85encode as base85
from base58 import b58encode as base58
import random

def multibase(secret_text: bytes) -> bytes:
    baselist = ['base32', 'base64', 'base58', 'base85']
    for _ in range(8):
        choice = random.choice(baselist)
        secret_text = eval(choice + '(secret_text)')

    return secret_text