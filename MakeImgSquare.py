from PIL import Image


def make_square(im, fill_color=(255, 255, 255, 0)):
    x, y = im.size
    size = max(x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


img = Image.open('./assets/hot.png')
square_img = make_square(img)
square_img.save('./assets/hot.png')
