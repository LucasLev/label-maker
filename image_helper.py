from PIL import Image, ImageDraw


def create_label(bg: Image.Image, text: str, text_font, text_color) -> Image.Image:
    """Create a label with text on a background image

    Note: This creates a new image with the text on top of the background image.
    No changes are made to the original background image.

    Parameters
    ----------
    bg : Image.Image
        The background image
    text : str
        The text to be displayed on the label
    text_font :
        The font to be used for the text
    text_color :
        The color of the text

    Returns
    -------
    Image.Image
        The label with the text
    """
    bg = bg.copy()
    dr = ImageDraw.Draw(bg)

    dr.text(
        (bg.width // 2, bg.height // 2),
        text,
        font=text_font,
        fill=text_color,
        anchor="mm",
    )
    return bg


def image_grid(imgs: list[Image.Image], rows: int, cols: int) -> Image.Image:
    """Generate a grid of images

    Parameters
    ----------
    imgs : list[Image.Image]
        The list of images to be arranged in a grid
    rows : int
        The number of rows in the grid
    cols : int
        The number of columns in the grid

    Returns
    -------
    Image.Image
        The grid of images
    """
    # assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new("RGBA", size=(cols * w, rows * h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid
