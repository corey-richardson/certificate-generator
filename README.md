# generator.py

## Imports

- warnings
    - `import warnings`
    - Used to disable the 'DeprecationWarning' warning in the terminal. This is definetly not best practice however... oh well.
- pandas
    - `import pandas as pd`
    - Used to read and manage the user information passed in from `information.csv` as a dataframe.
- pillow
    - `from PIL import Image, ImageDraw, ImageFont`
    - Used for image manipulation.

---

## Setup Variables

```py
font_name = "WinterSong-owRGB.ttf"
font_size = 200
text_y_pos = 270
tagline_FONT_TYPE = "calibri.ttf"
tagline_font_size = 48
tagline_spacing = 390

PREFIX = "assets/"
FONT_TYPE = PREFIX +  font_name
```

Set fonts, text sizes and spacings between lines. <br>
Constants `PREFIX` and `FONT_TYPE` are NOT to be changed.

--- 

## Main

- Reads CSV data into a datafram using pandas module.
    - `information_df = pd.read_csv("information.csv")`
- Iterates through each row in the `first_name` column of `information.csv` and passes the name as a parameter of the function `make_cert`.
- Once it has iterated through each name, prints an output message `"Finished creating certificates!"`

---

## Make Cert[ificate]

- Sets `draw` and `img_width` as global variables to be used in `write_subline()`.
- Opens the base image and saves to `img`.
- Saves the width of the image to `img_width`. This is used when centrally aligning text.
- Creates a 'draw object'.
- Creates a font object with arguments assigned in 'setup variables'.
- Gets the text width of the name. This is used when centrally aligning text.
- Draws the text onto the base image
- Sublines
    - Initialises / resets `line_num` to 0.
    - Calls `write_subline()` twice^, passing in the text to write and the current line number as arguments.
    - This function returns an incremented `line_num` which gets called by the next function call.
- Saves the manipulated image into the 'out' directory.

> ^I have it calling twice. If you want more than two line of text then you will have to call it that many times.

--- 

## Write Subline

- Creates a font object with arguments assigned in 'setup variables'.
- Gets the text width. This is used to centrally align the text.
- Draws the text onto the image.
    - `+ (50*line_num)` for each new line it will add 50 pixels of spacing between the previous line of text. `line_num` is zero indexed.
- Returns `line_num + 1`; this value gets called by the next function call.

---

# add_names.py

```py
# ctrl+c / keyboard interrupt to stop

with open("information.csv","a") as info_file:
    while True:
        name = input("child first name: ")
        guardian_name = input("guardian full name: ")
        email = input("email: ")
            
        to_write = f"\n{name.title()},{guardian_name.title()},{email.lower()},"
        info_file.write(to_write)
        print("added " + to_write)
```

This script is used to write new entries into `information.csv`. Of course this could be done manually but this script produces a consistent format for all entries via data cleansing.

---

# Directory levelling

- assets
    - base image [cert.jpg]
    - font [.tff]
- out
    - This is where the manipulated images will be saved to.
- add_names.py
- generator.py
- information.csv
- README.md [you are here]
