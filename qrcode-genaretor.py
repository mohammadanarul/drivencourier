import qrcode
funny = {
    'name': 'Md Anarul',
    'age': 20,
    'Sex': 'Male',
    'Country': 'Bangladesh',
}

img = qrcode.make(funny)
type(img)  # qrcode.image.pil.PilImage

img.save("funny.jpeg")