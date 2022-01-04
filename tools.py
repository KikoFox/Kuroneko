from PIL import Image, ImageDraw, ImageFont


def welcome_img(name):
    image = Image.open("img/sample.jpg")
    sample = image.resize((400, 200))
    idraw = ImageDraw.Draw(sample)
    title = ImageFont.truetype('font/friday13-bonus-nfi.ttf', size=18)

    idraw.text((75, 100), text=f'{name} just joined the server', font=title, fill="white")

    avatar_img = Image.open(f'img/profile_{name}.png')
    sample.paste(avatar_img, (150, 15), avatar_img)
    sample.save(f"img\profile_{name}.jpg")


def circle_avatar(img, name):

    width, height = img.size
    x = (width - height)//2
    img_cropped = img.crop((x, 0, x+height, height))

    mask = Image.new('L', img_cropped.size)
    mask_draw = ImageDraw.Draw(mask)
    width, height = img_cropped.size
    mask_draw.ellipse((0, 0, width, height), fill=255)

    img_cropped.putalpha(mask)

    img_cropped.save(f'img/profile_{name}.png')
