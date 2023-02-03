import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) # <-- bad lol

import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# setup variables
# name font
font_name = "WinterSong-owRGB.ttf"
font_size = 200
text_y_pos = 250
# sublines font
tagline_FONT_TYPE = "calibri.ttf"
# tagline_FONT_TYPE = "comic.ttf"
tagline_font_size = 48
tagline_spacing = 370

PREFIX = "assets/"
FONT_TYPE = PREFIX +  font_name

# MAIN FUNCTION
def main():
    # read the csv data into a dataframe named 'information_df'
    information_df = pd.read_csv("information.csv")
    
    # iterate through names in csv data and create certificate for each
    for i, name in enumerate(information_df.first_name):
        print(f"Creating certificate for {name}..... {i+1}/{len(information_df.index)}")
        make_cert(name)
    print("Finished creating certificates!")

# MAKE_CERT FUNCTION
def make_cert(name):
    global draw, img_width
    img = Image.open(f"{PREFIX}cert.jpg")
    img_width = img.width # get image dimensions
    
    # WRITE NAME
    draw = ImageDraw.Draw(img) # create draw object
    font_title = ImageFont.truetype( # create font object
        FONT_TYPE,
        font_size)
    # used for alingment centring
    text_width, _ = draw.textsize(name, font = font_title)
    draw.text( # write on image
            ( (img_width - text_width) / 2, text_y_pos),
            name, font = font_title, fill = "black")
    
    # WRITE SUB-LINES
    # SET SUB-LINE TEXT HERE
    line_num = 0
    line_num = write_subline("hello", line_num)
    line_num = write_subline("world", line_num)
    
    # output and save certificate as image
    img.save("out/{}.png".format(name.lower())) # save completed certificate to 'out/...'

# writes each sub line to the image
def write_subline(text_to_write, line_num):
    font_tagline = ImageFont.truetype(
        tagline_FONT_TYPE,
        tagline_font_size)
    # used for alingment centring
    text_width, _ = draw.textsize(text_to_write, font = font_tagline)
    draw.text( # write on image, for each line (zero indexed) add 50 pixels spacing
        ( (img_width - text_width) / 2, text_y_pos + tagline_spacing + (50*line_num)),
        text_to_write, font = font_tagline, fill = "black")
    return line_num + 1 # increment line num and return to be used by the next line
    
if __name__ == "__main__":
    main()
