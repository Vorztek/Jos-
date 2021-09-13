import qrcode

img = qrcode.make('https://www.instagram.com/lukpwarier3/')
type(img)  # qrcode.image.pil.PilImage
img.save('lulu.png')
