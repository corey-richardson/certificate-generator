import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) # <-- bad lol

import pandas as pd
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageFont

# setup variables
font_name = "WinterSong-owRGB.ttf"
font_type = "assets/" +  font_name # dont change this line
font_size = 160 # for name
text_y_pos = 100 # for name

message_subtitle = '''
Competed in Collins Aerospace's 'Invent A Model Plane Or Rocket' 
                    Competition During Engineers Week 2023'''
                
subtitle_font_type = "calibri.ttf"
subtitle_font_size = 25 # for subtitle
subtitle_spacing = 270 # for subtitle


def main():
    # information_file = fd.askopenfile(filetypes = (("CSV Files","*.csv"),))
    # information_df = pd.read_csv(information_file)
    
    # read the csv data into a dataframe named 'information_df'
    information_df = pd.read_csv("information.csv")
    num_rows = len(information_df.index) # get number of rows, used in progress bar
    
    for i, name in enumerate(information_df.first_name):
        print(f"Creating certificate for {name}..... {i+1}/{num_rows}") # progress bar
        make_cert(name)
    print("Finished creating certificates!")


def make_cert(name):
    img = Image.open("assets/cert.png")
    img_width = img.width # get image dimensions
    img_height = img.height
    draw = ImageDraw.Draw(img) # create draw object
    font_title = ImageFont.truetype( # create font object
        font_type,
        font_size)
    text_width, _ = draw.textsize(name, font = font_title) 
    draw.text( # write on image
            ( (img_width - text_width) / 2, text_y_pos),
            name, font = font_title, fill = "black")
    
    draw_subtitle = ImageDraw.Draw(img)
    font_subtitle = ImageFont.truetype( # create font object
        subtitle_font_type,
        subtitle_font_size)
    text_width, _ = draw_subtitle.textsize(message_subtitle, font = font_subtitle)
    draw.text( # write on image
        ( (img_width - text_width) / 2, text_y_pos + subtitle_spacing),
        message_subtitle, font = font_subtitle, fill = "black")


    img.save("out/{}.png".format(name.lower())) # save completed certificate to 'out/...'
        
main()

# 1280 x 720 reso
