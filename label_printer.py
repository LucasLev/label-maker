from itertools import batched
from json import load as json_load

from PIL import Image, ImageFont

from image_helper import create_label, image_grid

with open("plan_2024.json") as f:
    plan = json_load(f)


def label_generator(
    bg,
    letter,
    num_seats,
    text_font,
    text_color,
    *,
    txt_format="{letter}:{i}",
    parity="all",
):
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
            bg, txt_format.format(letter=letter, i=i), text_font, text_color
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
