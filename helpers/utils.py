import uuid
import qrcode
import random

SIX_NUMBER = random.randint(100000, 999999)
UNIQUE_TRAKING_NUMBER = str(uuid.uuid4()).replace('-', '').upper()[:12]

def bar_code_ganareotr(bar_code):
    b_img = qrcode.make(bar_code)
    b_img.save(f'{bar_code}.jpeg')
