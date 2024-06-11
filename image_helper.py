from PIL import Image, ImageDraw, ImageFont


def create_label(bg: Image, text, text_font: ImageFont, text_color):
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


def image_grid(imgs, rows: int, cols: int):
    # assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new("RGBA", size=(cols * w, rows * h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid
