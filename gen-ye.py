import textwrap
import sys
import os.path

from PIL import Image, ImageFont, ImageDraw
from functools import reduce

DEFAULT_COVER_IMAGE = 'ye-cover-hq.jpg'
DEFAULT_FONT_NAME = 'ye-font-regular.ttf'

def create_image(text, cover_img_name=DEFAULT_COVER_IMAGE, font_name=DEFAULT_FONT_NAME,
                font_size=120, text_color=(41,247,78), line_spacing=55):
    """
    Overlays text over the image corresponding to cover_img_name.
    Returns an Image object with the text overlay.
    """

    cover_img = Image.open(cover_img_name)
    draw = ImageDraw.Draw(cover_img)
    font = ImageFont.truetype(font_name, font_size)

    wrapped_text, max_line = wrap_text(text)

    W, H = cover_img.size
    print('"{}" (width={}, height={})'.format(cover_img_name, W, H))

    w, h = draw.textsize(max_line, font=font, spacing=line_spacing)
    print('text overlay (width={}, height={})'.format(w, h))

    w_c, h_c = (W - w) / 2, (H - h) / 2
    print('text centered at ({}, {})'.format(w_c, h_c))

    draw.multiline_text((w_c, h_c),
        wrapped_text,
        font=font,
        fill=text_color,
        align='center',
        spacing=line_spacing)

    del font
    del draw

    return cover_img

def wrap_text(text, max_width=15):
    """
    wraps text such that each line has a maximum
    width of 20 characters. Increases the spacing between
    each word.

    Returns the wrapped text along with the line with
    the greatest number of characters.
    """
    # expanded = map(lambda w : '  ' + w + '  ', text.split())
    # lines = textwrap.wrap(''.join(expanded), width=20)

    # TODO: handle new lines
    lines = textwrap.wrap(text, width=max_width)
    get_max_line = lambda x, y : x if len(x) > len(y) else y
    max_line = reduce(get_max_line, lines)

    print("text was split into {} line(s)".format(len(lines)))

    return '\n'.join(lines), max_line

def precondition(predicate, msg="Illegal Argument Exception"):
    """
    Basic precondition helper that raises
    an exception if the predicate is false.
    """
    if not predicate:
        raise Exception(msg)

def main():
    precondition(os.path.isfile(DEFAULT_COVER_IMAGE), "Cover not found.")
    precondition(os.path.isfile(DEFAULT_FONT_NAME), "Font not found.")

    text = sys.stdin.read()
    my_ye = create_image(text)
    my_ye.save('my-ye.jpg')
    print('Saved image to "my-ye.jpg"')

if __name__ == '__main__':
    main()