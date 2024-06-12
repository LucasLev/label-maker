from itertools import batched
from json import load as json_load
from typing import Iterator, Literal

from PIL import Image, ImageFont

from image_helper import create_label, image_grid

with open("plan_2024.json") as f:
    plan = json_load(f)


def label_generator(
    bg: Image.Image,
    row_name: str,
    num_seats: int,
    text_font,
    text_color,
    *,
    txt_format: str = "{row_name}:{i}",
    parity: Literal["odd", "even", "all"] = "all",
) -> Iterator[Image.Image]:
    """Generate labels for a row

    Parameters
    ----------
    bg : Image.Image
        The background image used for the labels
    row_name : str
        The name of the row
    num_seats : int
        The number of seats in the row
    text_font : _type_
        The font to be used for the text
    text_color : _type_
        The color of the text
    txt_format : str, optional
        The format string used for the labels, by default "{row_name}:{i}"
    parity : Literal["odd", "even", "all"], optional
        Flag to determine specific label generation (only odd, only even, or all), by default "all"

    Yields
    ------
    Iterator[Image.Image]
        An iterator of labels
    """
    match parity:
        case "odd":
            start = 1
            step = 2
        case "even":
            start = 2
            step = 2
        case "all" | _:
            start = 1
            step = 1

    for i in range(start, num_seats + 1, step):
        yield create_label(
            bg, txt_format.format(row_name=row_name, i=i), text_font, text_color
        )


lan_ets_orange = (255, 136, 17)
lan_ets_font = ImageFont.truetype("BravePhoenix.ttf", 256)

bg = Image.open("background.png")

images = []
for letter, num_seats in plan.items():
    images.append(
        label_generator(
            bg, letter, num_seats, lan_ets_font, lan_ets_orange, parity="odd"
        ),
    )
    images.append(
        label_generator(
            bg, letter, num_seats, lan_ets_font, lan_ets_orange, parity="even"
        ),
    )


nb_rows = 4
nb_cols = 3
grids = (
    image_grid(sub_row, nb_rows, nb_cols)
    for row in images
    for sub_row in batched(row, nb_cols * nb_rows)
)

first = next(grids)
first.save(
    "out.pdf",
    optimize=True,
    resolution=first.width / 8.5,
)
for grid in grids:
    grid.save(
        "out.pdf",
        optimize=True,
        resolution=grid.width / 8.5,
        append=True,
    )
