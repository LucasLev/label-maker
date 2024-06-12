# Lan ETS - Label Generator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Generates all the labels needed to mark the BYOC section.

Labels are grouped by row and parity.

## Dependencies

You can install all dependencies using :

```Bash
pip install -r requirements.txt
```

<sub> Tiny rant : Pip SHOULD (in a perfect world) be able to download them from [pyproject.toml](pyproject.toml). [Maybe](https://github.com/pypa/pip/issues/11440#issuecomment-1445119899) [one day](https://peps.python.org/pep-0735/).</sub>

## Setup

The main program [label_printer.py](label_printer.py) takes as input a json file, a background, a font, and a color.

The json file represent the seating plan. It is expected to be of the following format :

```json
{
    "A" : 12, //number of seats
    "B" : 24,
}
```

You can name the rows however you see fit, but their full name will be used when generating the label so I would advise to keep it to 2 characters or less. You can use [plan_2024.json](plan_2024.json) as an example.

The background is assumed to have the correct aspect ratio (and DPI) to fit onto a US Letter standard sheet of paper when laid out in the selected grid configuration. The background is used for every label (NOT 1 background / grid). The background for the 2024 edition is [background.png](background.png).

The font is used to add the label onto the background. It should be in TrueType (``.ttf``) or OpenType (``.otf``). The font for the 2024 edition is [bravephoenix.ttf](bravephoenix.ttf).

The color is the color of the text applied to the background. The Lan ETS orange is used : ``#FF8811``.

The programmes outputs all the label into a PDF named ``out.pdf``.

> [!CAUTION]
> If there is already a document named "out.pdf", it WILL be overwritten.
