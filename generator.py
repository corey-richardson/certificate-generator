import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) # <-- bad lol

import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# setup variables
# name font
font_name = "WinterSong-owRGB.ttf"
font_size = 100 # 200
text_y_pos = 450 #270
# sublines font
tagline_FONT_TYPE = "calibri.ttf"
# tagline_FONT_TYPE = "comic.ttf"
tagline_font_size = 20 # 48
tagline_spacing = 180 # 390

PREFIX = "assets/"
FONT_TYPE = PREFIX +  font_name

# MAIN FUNCTION
def main():
    try:
        # read the csv data into a dataframe named 'information_df'
        input_file = "information.csv"
        information_df = pd.read_csv(input_file)
    except FileNotFoundError: # if "information.csv" not automatically found, show a warning box and then
                              # get the user to manually enter an information / input file
        mb.showwarning(title="FileNotFoundError", \
            message="Failed to find 'information.csv' in current directory, please select manually.")
        input_file = fd.askopenfilename(filetypes=[("CSV files", "*.csv")],title="Set input .csv file")
        information_df = pd.read_csv(input_file)
        
    # get output directory to save certificates to
    global output_dir
    output_dir = fd.askdirectory(title="Set output folder")
    print(output_dir)

    # iterate through names in csv data and create certificate for each
    for i, name in enumerate(information_df.first_name):
        print(f"Creating certificate for {name}..... {i+1}/{len(information_df.index)}")
        make_cert(name)
        information_df["file_path"][i] = f"{output_dir}/{name}.png"
    information_df.to_csv(input_file, index=False)
    mb.showinfo("Done!","Finished creating certificates!")
    os.startfile(output_dir)

# MAKE_CERT FUNCTION
def make_cert(name):
    global draw, img_width
    img = Image.open(f"{PREFIX}Slide1.png")
    img_width = img.width # get image dimensions
    
    # WRITE NAME
    draw = ImageDraw.Draw(img) # create draw object
    font_title = ImageFont.truetype( # create font object
        FONT_TYPE,
        font_size
        )
    # used for alingment centring
    text_width, _ = draw.textsize(name, font = font_title)
    draw.text( # write on image
            ( (img_width - text_width) / 2, # (for left/right alignment)
            text_y_pos),
            name, font = font_title, fill = "black")
    
    # WRITE SUB-LINES
    # SET SUB-LINE TEXT HERE
    line_num = 0
    # line_num = write_subline("hello", line_num) # multi line
    # line_num = write_subline("world", line_num)
    
    line_num = write_subline("hello world", line_num) # single line

    # output and save certificate as image
    img.save(f"{output_dir}/{name.lower()}.png") # save completed certificate to 'out/...'

# writes each sub line to the image
def write_subline(text_to_write, line_num):
    font_tagline = ImageFont.truetype(
        tagline_FONT_TYPE,
        tagline_font_size)
    # used for alingment centring
    text_width, _ = draw.textsize(text_to_write, font = font_tagline)
    draw.text( # write on image, for each line (zero indexed) add 50 pixels spacing
        ( (img_width - text_width) / 2, # + 350 (for left/right alignment)
        text_y_pos + tagline_spacing + (50*line_num)),
        text_to_write, font = font_tagline, fill = "black")
    return line_num + 1 # increment line num and return to be used by the next line
    
if __name__ == "__main__":
    main()
