import qrcode
import uuid
lol_id = str(uuid.uuid4()).replace('-', '').upper()[:12]
funny = lol_id

# img = qrcode.make(funny)
# type(img)  # qrcode.image.pil.PilImage

# img.save("funny.jpeg")


def bar_code_ganareotr(lol):

    b_img = qrcode.make(lol)
    b_img.save(f'{lol}.jpeg')


a = 12
b = 10
num_sum = a + b


