import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import pandas as pd
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageFont

# setup variables
font_name = "WinterSong-owRGB.ttf"
font_type = "assets/" +  font_name # dont change
font_size = 500
text_y_pos = 2000

def main():
    # information_file = fd.askopenfile(filetypes = (("CSV Files","*.csv"),))
    # information_df = pd.read_csv(information_file)
    
    information_df = pd.read_csv("information.csv")
    num_rows = len(information_df.index)
    
    for i, name in enumerate(information_df.first_name):
        print(f"Creating certificate for {name}..... {i+1}/{num_rows}")
        make_cert(name)
    print("Finished creating certificates!")


def make_cert(name):
    img = Image.open("assets/cert.png")
    img_width = img.width # get image dimensions
    img_height = img.height
    draw = ImageDraw.Draw(img) # create draw object
    font = ImageFont.truetype( # create font object
        font_type,
        font_size
    )
    
    text_width, _ = draw.textsize(name, font = font) 
    draw.text( # write on image
            ( (img_width - text_width) / 2, text_y_pos),
            name, font = font, fill = "black")

    img.save("out/{}.png".format(name.lower())) # save completed certificate to out/
        
main()