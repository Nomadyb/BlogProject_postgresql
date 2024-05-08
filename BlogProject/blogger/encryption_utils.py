
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from django.conf import settings


def encrypt_image(image_path):
    cipher = AES.new(settings.KEY, AES.MODE_ECB)
    with open(image_path, 'rb') as f:
        image_data = f.read()
    padded_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return b64encode(encrypted_data)


def decrypt_image(encrypted_data):
    pass